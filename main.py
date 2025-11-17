from fastapi import FastAPI

app = FastAPI()

@app.get("/{context_id}")
def get_policy(context_id: str):
    return [
        {"mam": 150.0, "asking_price": 200.0},
        {"mam": 140.0, "asking_price": 190.0},
        {"mam": 130.0, "asking_price": 180.0},
        {"mam": 120.0, "asking_price": 170.0},
    ]
