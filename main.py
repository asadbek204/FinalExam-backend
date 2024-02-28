import uvicorn
from fastapi import FastAPI
from routers import router
from settings import settings

app = FastAPI()
app.include_router(router)


def main(host: str = settings.server.domain, port: int = int(settings.server.port)):
    uvicorn.run('main:app', host=host, port=port, reload=True)


if __name__ == "__main__":
    main()
