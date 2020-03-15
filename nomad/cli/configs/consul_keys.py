import subprocess

DOCKER_IMAGES_SERVER_PORT = 8006

result = subprocess.run(['id', '-u'], stdout=subprocess.PIPE)
USER_ID = int(result.stdout)
result = subprocess.run(['id', '-g'], stdout=subprocess.PIPE)
GROUP_ID = int(result.stdout)

# USER_ID=$(id -u)
# GROUP_ID=$(id -g)

consul_keys = {
    'nomad-': {
        'USER_ID': f"{USER_ID}",
        'GROUP_ID': f"{GROUP_ID}",
        'GET_IDS_USING_CONSUL': "yes",
        'resources_register_host': f'http://localhost:{DOCKER_IMAGES_SERVER_PORT}',
        'postgres_pgdata': '/home/a/dockers-data/sb-postgres',
        'files_service_app_data': '/home/a/src/a/sb/POCs/gateways-poc/services/files_service/priv/files',
        # 'krakend_config_data': '/home/a/src/a/sb/POCs/gateways-poc/devOps/krakend',
        # 'krakend_config_data': '/home/a/src/POCs/krakend',

        'krakend_config_data': '/home/a/Desktop/poc/wiremock/krakend',
        'files_and_mappings_root_wiremock': '/home/a/Desktop/poc/wiremock/working-dir',
        'files_and_mappings_root_wiremock_webhook': '/home/a/Desktop/poc/wiremock/working-dir-webhook',

        'dev_env_directory_e': '/home/a/src/a/sb/dev/paygate',
        'dev_env_directory_h': '/media/a/data/docs-files/Web/Testing/proxies/service-virtualization/wiremock/webhooks',
        'dev_env_direnv_alloweds': '/home/a/Desktop/poc/dev_env/.local/share/direnv/allow',

        'php_dev_env_directory': '/home/a/Downloads/src/php/',
        'dev_env_directory_elixir': '/home/a/src/POCs/distributed-computing/',

        'templates_webhook_transformer': '/home/a/src/ansible/src/micro/py/templates',
        'fluentd_etc': '/home/a/dockers-data/fluentd/td-agent',
        'elasticsearch_config': '/home/a/dockers-data/elasticsearch/config',
        'elasticsearch_data': '/home/a/dockers-data/elasticsearch/data',

        'rabbitmq_enabled_plugins': '/home/a/dockers-data/sb-rabbitmq_plugins/sb-enabled_plugins',
        'rabbitmq_data': '/home/a/dockers-data/sb-rabbitmq',
        'nexus_data': '/home/a/dockers-data/nexus-data',

        'spark_apps': '/home/a/Downloads/course/spark_apps',

        'verdaccio_storage': '/home/a/dockers-data/npm/storage',
        'verdaccio_conf': '/home/a/dockers-data/npm/conf',
        'DOCKER_IMAGES_SERVER_PORT': f'{DOCKER_IMAGES_SERVER_PORT}',
    },

    'flask-common-': {
        'LOCAL': 'Yes',
        'FLASK_APP': 'app.py',
        'GENERATE_POSTMAN_COLLECTION': 'yes',
    },

    'mitmproxy-config-': {
        'MITMPROXY_PORT': '8082',
        'MITMPROXY_WEB_UI_PORT': '8083',
    },
    'toxiproxy-config-': {
        'TOXIPROXY_SERVER_PORT': '8474',
    },
    'hoverfly-config-': {
        'HOVERFLY_PROXY_PORT': '8501',
        'HOVERFLY_ADMIN_PORT': '8888',
    },
    'gor-config-': {
        'GOR_INPUT_RAW_PORT': '8600',
        # 'GOR_INPUT_RAW_PORT': '80',
        # 'GOR_INPUT_RAW_PORT': '4000',
        # 'GOR_INPUT_RAW_PORT': '56299',
        'GOR_OUTPUT_PATH': '/home/a/src/a/sb/QA/gateway/payment-gateways/service-virtualization/gor/requests.gor',
    },
    'haproxy-config-': {
        'HAPROXY_CONFIG_PATH': '/media/a/data/docs/Web/High-Performance/LB/HA-Proxy/haproxy/',
    },
    'prometheus-config-': {
        'PROMETHEUS_HOME': '/home/a/appslnx/monitoring/prometheus-2.x/',
    },
    'grafana-config-': {
        'GRAFANA_HOME': '/home/a/appslnx/monitoring/grafana-6.x/bin/',
    },
    'node_exporter-config-': {
        'NODE_EXPORTER_HOME': '/home/a/appslnx/monitoring/node_exporter-0.x/',
    },
    'grok_exporter-config-': {
        'GROK_EXPORTER_HOME': '/home/a/appslnx/monitoring/grok_exporter-0.x/',
    },

}
