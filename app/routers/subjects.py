import time
from fastapi import APIRouter
from app.metrics import SUBJECT_ACCESS_HISTOGRAM
from app.models import Subject
from app.fake_db import subjects

router = APIRouter()

@router.get("/", response_model=list[Subject])
def get_subjects():
    with SUBJECT_ACCESS_HISTOGRAM.labels(subject="all").time():
        time.sleep(0.1)
        return subjects