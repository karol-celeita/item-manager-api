import uvicorn
from constants import HOST_API, PORT_API, RELOAD, API_VERSION
from fastapi import FastAPI

app = FastAPI(
    title="API",
    description="Item Manager",
    version=API_VERSION,
    redoc_url=None,
    docs_url="/api/v1/docs",
)

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host=HOST_API,
        port=PORT_API,
        reload=RELOAD,
    )
    