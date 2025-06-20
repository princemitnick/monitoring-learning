from fastapi import APIRouter
from app.models import Subject
from app.fake_db import subjects

router = APIRouter()

@router.get("/", response_model=list[Subject])
def get_subjects():
    return subjects