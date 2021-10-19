from fastapi import FastAPI

app = FastAPI()

items = ["Cachorro", "Gato", "Rato", "Unicornio"]

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id - 1 >= len(items): raise Exception("Invalid Item Id")
    return {"item": items[item_id]}