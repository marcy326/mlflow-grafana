# Proxy Server with Monitoring

This project provides a proxy server for MLflow model server requests and a monitoring system using Grafana.

## Features

- Proxy server receives requests from clients and forwards them to the MLflow model server.
- Request and response data are stored in Loki.
- Grafana dashboard allows monitoring of metrics such as model prediction rates.

## Components

This project consists of the following components:

- `proxy`: Flask-based proxy server
- `inference`: MLflow model server
- `loki`: Log collection system
- `promtail`: Agent for sending logs to Loki
- `grafana`: Monitoring dashboard

These components are launched using Docker Compose.

## Usage

1. Clone this repository.
2. Run `docker compose up -d` to start all components.
3. Access Grafana (http://localhost:3000) and log in (username: `admin`, password: `admin`).
4. Check the dashboard to monitor metrics such as model prediction rates.
5. To send requests to the proxy server, you can use the `request_example.sh` script.

## Notes

- Proxy server logs are stored in the `/proxy/logs` directory.
- Grafana dashboard and data source configurations are defined in files within the `grafana/` directory.
- Promtail configuration is defined in the `promtail-config.yaml` file.

## Future Enhancements

-[ ] Extend to support multiple models
-[ ] Add more detailed metrics on model accuracy and performance
-[ ] Implement alerting functionality
-[ ] Add operational features such as auto-scaling
