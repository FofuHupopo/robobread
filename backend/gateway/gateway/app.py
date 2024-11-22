from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.accounting import routes as accounting
from .routers.analytics import routes as analytics
from .routers.machines import routes as machines
from .routers.packing import routes as packing


app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "https://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(accounting.router, prefix="/accounting")
app.include_router(analytics.router, prefix="/analytics")
app.include_router(machines.router, prefix="/machines")
app.include_router(packing.router, prefix="/packing")


@app.get("/", tags=["Gateway"])
async def index():
    return {"message": "API Gateway"}
