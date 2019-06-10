#!/usr/bin/env bash

java ${JAVA_OPTS} -cp "lib/*" com.github.tomakehurst.wiremock.standalone.WireMockServerRunner --verbose --record-mappings --extensions org.wiremock.webhooks.Webhooks --port 80
