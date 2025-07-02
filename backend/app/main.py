from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.routers import auth
from app.dependencies import get_db

app = FastAPI(title="Stereo Paradise API")

app.include_router(auth.router)

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/health")
def health(db: Session = Depends(get_db)):
    return {"db_connection": db is not None}