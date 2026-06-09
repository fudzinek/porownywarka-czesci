from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Porownywarka dziala"}

@app.get("/price/{part_number}")
def get_price(part_number: str):
    return {
        "part_number": part_number,
        "results": [
            {"hurtownia": "Inter Cars", "cena_netto": 245.20, "stan": 12},
            {"hurtownia": "Auto Partner", "cena_netto": 238.10, "stan": 8},
            {"hurtownia": "Hart", "cena_netto": 251.40, "stan": 5},
        ]
    }
