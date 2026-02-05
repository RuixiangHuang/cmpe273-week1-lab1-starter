from fastapi import FastAPI

app = FastAPI()

# uvicorn main:app --reload --host 127.0.0.1 --port 8000

@app.get("/ping")
def ping():
    return {"message": "pong1"}

@app.get("/echo")
def echo(msg: str):
    return {"echo from service 1": msg}