from fastapi import FastAPI
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from app.routers import students, teachers, subjects, mappings
from fastapi.responses import Response
from app.metrics import MetricMiddleware, update_business_metrics

app = FastAPI(title="Student Monitoring API")

app.add_middleware(MetricMiddleware)

app.include_router(subjects.router, prefix="/subjects", tags=["Subjects"])
app.include_router(teachers.router, prefix="/teachers", tags=["Teachers"])
app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(mappings.router, prefix="/mappings", tags=["Mappings"])

@app.get("/")
def root():
    return {"message": "Student Monitoring API"}

@app.get("/metrics")
def metrics():
    update_business_metrics()
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)