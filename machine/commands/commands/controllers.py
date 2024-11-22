from fastapi import APIRouter


router = APIRouter(
    prefix="/"
)


@router.get("/ping")
async def ping():
    return {"message": f"Pong"}
