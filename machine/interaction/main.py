import uvicorn
from interaction.utils import getenv


def main():
    uvicorn.run(
        "interaction.app:app",
        host=getenv("HOST"),
        port=int(getenv("PORT")),
        reload=True,
        workers=int(getenv("WORKERS")) or 1
    )


if __name__ == "__main__":
    main()
