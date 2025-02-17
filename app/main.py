import uvicorn
from constants import HOST_API, PORT_API, RELOAD, API_VERSION
from fastapi import FastAPI
from database import create_tables
from models.items import Item
from routers import items


app = FastAPI(
    title="API",
    description="Item Manager",
    version=API_VERSION,
    redoc_url=None,
    docs_url="/api/v1/docs",
)

@app.get("/ping", tags=["ping"], summary="Verify API is UP ", description="Verify API is UP")
async def root():
    return {"message": "pong"}

app.include_router(items.router)

if __name__ == "__main__":

    create_tables()
    
    uvicorn.run(
        "main:app",
        host=HOST_API,
        port=PORT_API,
        reload=RELOAD,
    )
    