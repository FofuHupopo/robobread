import uvicorn
from commands.utils import getenv


def main():
    uvicorn.run(
        "commands.app:app",
        host=getenv("HOST"),
        port=int(getenv("PORT")),
        reload=True,
        workers=int(getenv("WORKERS")) or 1
    )


if __name__ == "__main__":
    main()
