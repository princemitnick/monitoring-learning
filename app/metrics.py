from prometheus_client import Counter, Histogram
import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

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

class MetricMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        endpoint = request.url.path
        REQUEST_COUNT.labels(request.method, endpoint).inc()
        REQUEST_LATENCY.labels(endpoint).observe(process_time)
        return response

