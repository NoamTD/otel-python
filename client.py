#!/usr/bin/env python3

import json
import requests
from opentelemetry import trace
from opentelemetry.instrumentation.requests import RequestsInstrumentor

from lib.otel import init_telemetry

RequestsInstrumentor().instrument()

init_telemetry("client.otel.tls.noamtd.github.com")

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("get_item") as span:
    response = requests.get(url="http://127.0.0.1:8000/items/4").json()
    span.add_event("got response", {"response": json.dumps(response)})

