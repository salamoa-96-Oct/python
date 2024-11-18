from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas
from app.db.session import get_db

router = APIRouter()

@router.post("/signup", response_model=schemas.UserRead)
def create_user(user_in: schemas.UserCreate, db=Depends(get_db)):
    conn, cursor = db  # 수정된 부분
    user = crud.get_user_by_email(conn, cursor, email=user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")
    new_user = crud.create_user(conn, cursor, user_in=user_in)
    return new_user
