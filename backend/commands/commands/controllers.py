from typing import Dict, Any

from fastapi import APIRouter
from fastapi import WebSocket
from fastapi.responses import HTMLResponse
from fastapi.websockets import WebSocketDisconnect


router = APIRouter()

clients: Dict[str, WebSocket] = {}

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()

    clients[client_id] = websocket

    try:
        while True:
            text = await websocket.receive_text()
            print(text)
            await websocket.send_text(text)
    except WebSocketDisconnect:
        del clients[client_id]


@router.post("/command/{client_id}")
async def send_data(client_id: str, data: dict[str, Any]):
    if client_id in clients:
        websocket = clients[client_id]
        await websocket.send_text(data)

        response = await websocket.receive_text()
        return {"response": response}
    else:
        return {"error": "Client not connected"}, 404
