import requests
import os
import sys

curr_dir = os.path.abspath(os.path.dirname(__file__))
app_dir = os.path.join(curr_dir, 'cli')

sys.path.append(app_dir)

from consul_keys import consul_keys

# nomad_keys = json.loads(open("./cli/consul-variables.json").read())

for prefix, variables in consul_keys.items():
    for key, value in variables.items():
        # response = requests.put(f"http://localhost:8500/v1/kv/{prefix}{key}",
        response = requests.put(f"http://172.17.0.2:8500/v1/kv/{prefix}{key}",
                                data=str.encode(value))
        # print(response.text)
