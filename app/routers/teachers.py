from fastapi import APIRouter
from app.models import Teacher
from app.fake_db import teachers

router = APIRouter()

@router.get("/", response_model=list[Teacher])
def get_teachers():
    return teachers
