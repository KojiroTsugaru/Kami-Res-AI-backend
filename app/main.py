from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Kami-Res-AI FastAPI backend is running."} 