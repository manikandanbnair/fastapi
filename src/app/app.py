from fastapi import FastAPI
import uvicorn
from .endpoints import all_router
app = FastAPI()


app.include_router(all_router)

def run_api():
    uvicorn.run(
        "app.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )