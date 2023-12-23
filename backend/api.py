##################################################
# 1. `python -m venv .venv`                      #
# 2. `.venv/Scripts/activate`                    #
# 3. `python -m pip install -r requirements.txt` #
# 4. `uvicorn api:app --reload`                  #
# 5. `deactivate`                                #
##################################################
import requests

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def products(draw: int, start: int = 0, length: int = 10):
    products = get_products()
    paginated = products[start:start + length]
    return { 
        "data": paginated, 
        "draw": draw,
        "recordsTotal": len(products),
        "recordsFiltered": len(products),
    }

def get_products():
    response = requests.get("https://dummyjson.com/products")
    json = response.json()
    attrs = ["id", "title", "description", "category", "price"]
    products = map(lambda p: { 
        attr: p[attr] for attr in attrs 
    }, json["products"])
    return list(products)