from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

items = ["Cachorro", "Gato", "Rato", "Unicornio"]


@app.get("/items/cachorro")
async def get_cachorro():
    return {"item": items[0]}

@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    if item_id - 1 >= len(items): raise Exception("Invalid Item Id")
    return {"item": items[item_id - 1]}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
