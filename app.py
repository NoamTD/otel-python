from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from lib.otel import init_telemetry

app = FastAPI()

init_telemetry("app.otel.tls.noamtd.github.com")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def root(item_id: int):
    return {"item_id": item_id}

FastAPIInstrumentor.instrument_app(app)