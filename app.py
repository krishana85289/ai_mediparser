from fastapi import FastAPI
from aiparser_end_points.endpoints import router as resume_router

app = FastAPI(
    title="Doctor Resume API",
    description="API for processing doctor resumes and monitoring system health."
)

app.include_router(resume_router, prefix="/api")
