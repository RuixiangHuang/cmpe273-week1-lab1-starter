from fastapi import FastAPI
import requests
import os

app = FastAPI()
# uvicorn second_main:app --reload --host 127.0.0.1 --port 8001
SERVICE_A_HOST = os.getenv("SERVICE_A_HOST", "127.0.0.1")

@app.get("/ping")
def ping():
    return {"message": "pong2"}


@app.get("/call-echo")
def call_echo(msg: str):
    resp = requests.get(
        f"http://{SERVICE_A_HOST}:8000/echo",
        params={"msg": msg},
        timeout=3
    )
    return resp.json()