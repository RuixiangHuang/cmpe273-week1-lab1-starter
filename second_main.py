from fastapi import FastAPI
import requests

app = FastAPI()
# uvicorn second_main:app --reload --host 127.0.0.1 --port 8001
@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"hello": name}

@app.get("/call-echo")
def call_echo(msg: str):
    resp = requests.get(
        "http://127.0.0.1:8000/echo",
        params={"msg": msg},
        timeout=3
    )
    return resp.json()