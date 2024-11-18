from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    created_user = crud.create_user(db, user)
    if created_user is None:
        raise HTTPException(status_code=500, detail="User could not be created")
    return created_user

@router.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db=Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/", response_model=list[schemas.UserRead])
def read_users(skip: int = 0, limit: int = 10, db=Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users