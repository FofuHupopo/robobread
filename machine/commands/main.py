import asyncio

from commands.app import connect_to_websocket


def main():
    client_id = "client1"
    asyncio.run(connect_to_websocket(client_id))


if __name__ == "__main__":
    main()
