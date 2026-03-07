from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# Instance of the fast api
app = FastAPI(title="Item Inventory")

@app.post('/items/')
async def create_item(item: Item):
    return item
