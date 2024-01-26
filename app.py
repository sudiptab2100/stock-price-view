from fastapi import FastAPI
from preset import preset
from db import get_top_k, get_favourites, add_favourite, remove_favourite, search_by_name
import uvicorn


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/search/{name}")
def search(name: str):
    return search_by_name(name)

@app.get("/get_top_k/{k}")
def get_tops(k: int):
    return get_top_k(k)

@app.get("/get_favourites")
def get_favs():
    favs = get_favourites()
    return favs

@app.post("/add_favourite/{stock_code}")
def add_fav(stock_code: int):
    add_favourite(stock_code)
    return {"message": "Added to favourites"}

@app.delete("/remove_favourite/{stock_code}")
def remove_fav(stock_code: int):
    remove_favourite(stock_code)
    return {"message": "Removed from favourites"}


if __name__ == "__main__":
    preset(days=50, refresh=False)
    uvicorn.run(app, host="0.0.0.0", port=8000)