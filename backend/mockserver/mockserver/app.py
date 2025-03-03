from fastapi import FastAPI

from .routers import sales


app = FastAPI()
app.include_router(sales.router, prefix="/api/mockserver/sales", tags=["mockserver"])


@app.get("/")
async def root():
    return {"message": "Mock Server"}
