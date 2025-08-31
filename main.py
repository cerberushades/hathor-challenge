# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import services

app = FastAPI(title="Hathor Counter API", description="This API can be used to create a list of numbers and manipulate each of its elements.", version="1.0.0")


class CounterInit(BaseModel):
    counter: int


class IndexPayload(BaseModel):
    index: int


@app.post("/start", tags=["List Manipulation Methods"])
def start_counter(payload: CounterInit):
    result = services.start_counter(payload.counter)
    return {"list": result}


@app.get("/value/{index}", tags=["List Manipulation Methods"])
def return_value(index: int):
    try:
        value = services.return_value(index)
        return {"index": index, "value": value}
    except IndexError:
        raise HTTPException(status_code=400, detail="Índice inválido")


@app.post("/increment", tags=["List Manipulation Methods"])
def increment(payload: IndexPayload):
    try:
        value = services.increment(payload.index)
        return {"index": payload.index, "new_value": value}
    except IndexError:
        raise HTTPException(status_code=400, detail="Índice inválido")


@app.post("/set_max", tags=["List Manipulation Methods"])
def set_max():
    result = services.set_max()
    return {"list": result}
