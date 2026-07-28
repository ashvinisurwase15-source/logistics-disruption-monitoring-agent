from fastapi import FastAPI
from backend.api.news_routes import router as news_router

app = FastAPI(
    title="EV Battery Supply Chain Monitor",
    description="Autonomous disruption monitoring system for the EV battery supply chain",
    version="1.0.0"
)
app.include_router(news_router)


@app.get("/")
def home():
    return {
        "message": "EV Battery Supply Chain Monitoring API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }