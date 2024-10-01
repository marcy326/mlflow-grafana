# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "/app/proxy_server.py", "--mlflow-model-server-uri", "http://inference:8080/invocations", "--log-dir", "/app/logs"]
