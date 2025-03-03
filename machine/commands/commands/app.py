import asyncio
import websockets


async def connect_to_websocket(client_id):
    uri = f"ws://localhost:8006/ws/{client_id}"
    
    async with websockets.connect(uri) as websocket:
        print("Connected to the WebSocket server.")

        async def receive_messages():
            print("hi")
            while True:
                message = await websocket.recv()
                print(f"Message from server: {message}")

        asyncio.create_task(receive_messages())

        while True:
            data = input("Enter data to send to server: ")
            await websocket.send(data)
            print(f"Sent: {data}")
