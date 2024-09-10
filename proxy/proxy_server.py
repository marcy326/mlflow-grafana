import sys
import os
import uuid
import requests
import logging
from datetime import datetime, date
import json
import click
from flask import Flask, request

app = Flask(__name__)
data_type = "application/json"

_log_dir = None
_mlflow_model_server_uri = None

# ログの設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)

def log_request_response(inp, out, log_dir):
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().isoformat()

    # 入力と出力のペアごとにログを記録
    for input_value, output_value in zip(inp["inputs"], out["predictions"]):
        log_entry = {
            "timestamp": timestamp,
            "input_data": input_value,
            "prediction": output_value
        }
        d_today = date.today()
        str_today = d_today.strftime('%Y%m%d')
        log_file = os.path.join(log_dir, f"log_{str_today}.json")
        with open(log_file, "a") as f:
            json.dump(log_entry, f)
            print('', file=f)
        logger.info(f"Logged data to {log_file}")

def call_mlflow_model_server(data):
    headers = { "accept": data_type, "Content-Type": data_type }
    rsp = requests.post(url=_mlflow_model_server_uri, data=json.dumps(data), allow_redirects=True, headers=headers)
    return json.loads(rsp.text)

@app.route("/invocations", methods=["POST"])
def process():
    inp = request.json
    out = call_mlflow_model_server(inp)
    log_request_response(inp, out, _log_dir)
    return json.dumps(out)

@click.command()
@click.option("--port", help="Port", type=int, required=True)
@click.option("--mlflow-model-server-uri", help="MLflow model server URI", type=str, required=True)
@click.option("--log-dir", help="Log directory", default="/var/log/proxy-server", type=str)
def main(port, mlflow_model_server_uri, log_dir):
    global _log_dir, _mlflow_model_server_uri
    _mlflow_model_server_uri = mlflow_model_server_uri
    _log_dir = log_dir
    app.run(debug=True, host="0.0.0.0", port=port)

if __name__ == '__main__':
    main()
