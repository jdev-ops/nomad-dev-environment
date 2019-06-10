#!/usr/bin/env bash

# docker run -d --rm --name=dev-consul -e CONSUL_UI_BETA=true consul:1.1.0
# docker run -d --rm --name=dev-consul --net host -e CONSUL_UI_BETA=true consul:1.1.0

docker run -d --rm --name=consul-dev --net host -enable-script-checks consul:1.5.1

# http PUT http://localhost:8500/v1/agent/service/register < wiremock-service.json
