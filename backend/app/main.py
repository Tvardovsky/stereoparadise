from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.routers import auth
from app.core.database import SessionLocal

app = FastAPI(title="Stereo Paradise API")

app.include_router(auth.router)

@app.get("/ping")
def ping():
    return {"message": "pong"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health(db: Session = Depends(get_db)):
    return {"db_connection": db is not None}