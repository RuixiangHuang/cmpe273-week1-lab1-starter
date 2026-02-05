from fastapi import FastAPI

app = FastAPI()

# uvicorn main:app --reload --host 127.0.0.1 --port 8000

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"hello": name}

@app.get("/echo")
def echo(msg: str):
    return {"echo": msg}