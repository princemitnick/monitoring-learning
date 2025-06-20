from fastapi import APIRouter
from app.fake_db import students
from app.models import Student

router = APIRouter()
@router.get("/", response_model=list[Student])
def get_students():
    return students