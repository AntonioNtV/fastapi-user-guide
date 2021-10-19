from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel 

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()

animals = ["Cachorro", "Gato", "Rato", "Unicornio"]

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
registered_items = []

@app.get("/animals/cachorro")
async def get_cachorro():
    return {"item": animals[0]}

@app.get("/animals/{animal_id}")
async def get_animal_by_id(animal_id: int):
    if animal_id - 1 >= len(animals): raise Exception("Invalid Item Id")
    return {"item": animals[animal_id - 1]}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/file/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/item/")
async def read_item(skip: int = 0, limit: int = 0):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def read_item_by_id(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    registered_items.append(item)
    return item_dict