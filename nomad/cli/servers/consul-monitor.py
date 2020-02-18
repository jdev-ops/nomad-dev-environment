from typing import Dict, Any, Set

from flask import Flask, request

app = Flask(__name__)
import requests
import time

from toposort import toposort, toposort_flatten
import json

from jinja2 import Environment, FileSystemLoader

import sys
import os
import subprocess

searchpath = os.getenv("nomad_working_dir")
# searchpath = "/home/a/src/devOps/nomad/"

env = Environment(
    loader=FileSystemLoader(searchpath=searchpath),
    trim_blocks=True, lstrip_blocks=True
)

global_consul_ip = "172.17.0.2"
consul_address = "localhost"


# curl -G http://localhost:8500/v1/agent/services --data-urlencode 'filter=Service == wiremock'

@app.route('/services', methods=["POST"])
def services():
    print("********")
    print(request.json)
    return {"state": "ok"}, 200


def update_ports():
    services_data = requests.get(f"http://{consul_address}:8500/v1/agent/services").json()

    for v in services_data.values():
        response = requests.put(f"http://{global_consul_ip}:8500/v1/kv/service-port-{v['Service']}",
                                data=str.encode(str(v['Port'])))


@app.route('/deploy', methods=["POST"])
def deployment():
    deps = request.json

    waiting_dict = {x: y for (x, y) in deps.items() if type(y) is int}
    deps = [(x, y) for (x, y) in deps.items() if type(y) is list]
    deps = dict(deps)

    deps = {k: set(v) for k, v in deps.items()}

    # print(list(toposort_flatten(deps)))
    new_services = list(toposort_flatten(deps))
    new_services = [(i.split("/")[0], i.split("/")[1]) for i in new_services]

    req = requests.get("http://127.0.0.1:8500/v1/agent/services")
    req = req.json()
    existing_services = []
    for k, v in req.items():
        if "Service" in v.keys():
            existing_services.append(v["Service"])

    existing_services = set(existing_services)

    new_services = [(prefix, service) for (prefix, service) in new_services if service not in existing_services]

    # print(new_services)

    # python cli/run-nomad-job.py "${filename}"
    for (prefix, service) in new_services:
        template_name = f"dev/{prefix}/{service}.nomad-job.template"
        template = env.get_template(template_name)

        params = os.environ
        res = template.render(
            **params
        )
        proc = subprocess.Popen(["nomad", "job", "run", "-"], stdin=subprocess.PIPE)
        msg = str.encode(str(res) + "\n")

        # print(f"SENDING: {msg}")

        out, err = proc.communicate(msg)

        time.sleep(5)

        update_ports()

        wtime = waiting_dict.get(f"{prefix}/{service}", None)
        if wtime:
            time.sleep(wtime)

    return {"state": "ok"}, 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
