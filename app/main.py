from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routes import router as api_router

app = FastAPI(debug=True)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return RedirectResponse(url="/docs") 