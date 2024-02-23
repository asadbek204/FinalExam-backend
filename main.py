import uvicorn
from fastapi import FastAPI
from routers import router

app = FastAPI()
app.include_router(router)


def main(host: str = "127.0.0.1", port: int = 8000):
    uvicorn.run('main:app', host=host, port=port, reload=True)


if __name__ == "__main__":
    main()
