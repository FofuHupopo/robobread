from fastapi import APIRouter
from mockserver.utils import read_json


router = APIRouter()


@router.get("")
def register():
    return read_json("sales.json")
