from fastapi import APIRouter
from app.models import StudentTeacherMapping
from app.fake_db import student_teacher_mapping

router = APIRouter()

@router.get("/", response_model=list[StudentTeacherMapping])
def get_mappings():
    return student_teacher_mapping