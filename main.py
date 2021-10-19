from fastapi import FastAPI

app = FastAPI()

items = ["Cachorro", "Gato", "Rato", "Unicornio"]


@app.get("/items/cachorro")
async def get_cachorro():
    return {"item": items[0]}

@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    if item_id - 1 >= len(items): raise Exception("Invalid Item Id")
    return {"item": items[item_id - 1]}