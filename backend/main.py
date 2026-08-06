from fastapi import FastAPI
from backend.api.news_routes import router as news_router
from backend.api.risk_routes import router as risk_router
from backend.api.supplier_routes import router as supplier_router
from backend.api.report_routes import router as report_router
from backend.api.graph_routes import router as graph_router
app = FastAPI(
    title="EV Battery Supply Chain Monitor",
    description="Autonomous disruption monitoring system for the EV battery supply chain",
    version="1.0.0"
)
app.include_router(news_router)
app.include_router(risk_router)
app.include_router(graph_router)
app.include_router(supplier_router)
app.include_router(report_router, tags=["Report"])


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