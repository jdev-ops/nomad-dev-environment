FROM jalbert/jdk:11

# the service can run without privileges,
# Creating a USER without non-root privileges.
RUN groupadd -g 1000 wiremock && \
    adduser -u 1000 -g 1000 -d /wiremock wiremock

RUN mkdir -p /wiremock/lib
RUN mkdir -p /wiremock/__files
RUN mkdir -p /wiremock/mappings

COPY lib /wiremock/lib
COPY start_command.sh /wiremock/start_command.sh

RUN chown -R wiremock:wiremock /wiremock

ENV JAVA_OPTS=""

EXPOSE 80

USER root
WORKDIR /wiremock

RUN chmod +x /wiremock/start_command.sh

ENTRYPOINT ["/bin/bash", "start_command.sh"]
