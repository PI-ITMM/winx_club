import uvicorn
from fastapi import Depends, FastAPI
from typing import Optional
from database import SessionLocal, engine
from crud import *


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Анкета для друзей",
    version="0.0.1"
)


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


@app.get("/profiles/")
def get_profiles(db: Session = Depends(get_db)):
    return crud_get_profiles(db)


@app.get("/profiles/{id}")
def get_profile(id: int, db: Session = Depends(get_db)):
    return crud_get_profile(id, db)


@app.post("/profile/")
def create_profile(profile: Profile, db: Session = Depends(get_db)):
    pass


@app.put("/profile/{id}")
def update_profile(id: int, profile: Profile = None, db: Session = Depends(get_db)):
    pass


@app.delete("/profile/{id}")
def delete_profile(id: int, db: Session = Depends(get_db)):
    pass


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)