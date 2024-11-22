from fastapi import FastAPI

from .routers import auth


app = FastAPI()
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])


@app.get("/")
async def root():
    return {"message": "Auth Service"}
