from prometheus_client import Counter, Histogram, Gauge
import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.fake_db import students, student_teacher_mapping

REQUEST_COUNT = Counter(
    "api_request_count",
    "Nombre total de request HTTP",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "api_request_latency_seconds",
    "Durée des request HTTP",
    ["endpoint"]
)

TOTAL_STUDENTS = Gauge(
    "total_students",
    "Nombre total d'étudiants dans fake_db"
)

TOTAL_MAPPINGS = Gauge(
    "total_student_teacher_mappings",
    "Nombre total de correspondances etudiants-professeur"
)

SUBJECT_ACCESS_HISTOGRAM = Histogram(
    "subject_access_duration_seconds",
    "Temps de traitement des requêtes par matière",
    ["subject"]
)

REQUESTS_BY_IP = Counter(
    "api_requests_by_ip_total",
    "Nombre total de requêtes par adresse IP",
    ["ip"]
)

class MetricMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        endpoint = request.url.path
        REQUEST_COUNT.labels(request.method, endpoint).inc()
        REQUEST_LATENCY.labels(endpoint).observe(process_time)
        client_ip = request.client.host
        REQUESTS_BY_IP.labels(client_ip).inc()

        return response

def update_business_metrics():
    TOTAL_STUDENTS.set(len(students))
    TOTAL_MAPPINGS.set(len(student_teacher_mapping))
