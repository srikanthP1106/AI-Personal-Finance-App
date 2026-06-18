from fastapi import FastAPI
from backend.api.income import router as income_router
from backend.api.expense import router as expense_router
from backend.api.balance import router as balance_router
from backend.api.summary import router as summary_router

app = FastAPI(
    title="AI Personal Finance API",
    version="1.0.0"
)

app.include_router(income_router)
app.include_router(expense_router)
app.include_router(balance_router)
app.include_router(summary_router)


@app.get("/")
def home():
    return {
        "message": "AI Personal Finance API Running Successfully"
    }