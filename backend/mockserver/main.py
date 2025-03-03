import uvicorn
from dotenv import load_dotenv

from mockserver.utils import getenv


def main():
    load_dotenv()

    uvicorn.run(
        "mockserver.app:app",
        host=getenv("HOST"),
        port=int(getenv("PORT")),
        reload=True,
        workers=int(getenv("WORKERS")) or 1
    )


if __name__ == "__main__":
    main()
