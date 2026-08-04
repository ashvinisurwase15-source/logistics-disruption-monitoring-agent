from fastapi import APIRouter
from backend.reports.report_agent import ReportAgent

router = APIRouter()


@router.get("/report")
def get_report():
    agent = ReportAgent()
    return agent.generate_report()