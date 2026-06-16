from fastapi import FastAPI
from backend.api.income import router as income_router

app = FastAPI(
    title="AI Personal Finance API",
    version="1.0.0"
)

app.include_router(income_router)

@app.get("/")
def home():
    return {
        "message": "AI Personal Finance API Running Successfully"
    }