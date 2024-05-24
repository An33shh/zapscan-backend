# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import router  # Make sure the path is correct

app = FastAPI()
app.include_router(router, prefix="/api")  # Include your router

# Mount static files for React (if you have any)
app.mount("/", StaticFiles(directory="zapscan-frontend/build"), name="static")  
