from fastapi import APIRouter

from backend.agents.orchestrator import SupplyChainOrchestrator


router = APIRouter()


@router.get("/orchestrator", tags=["Multi-Agent Orchestrator"])
def run_orchestrator():
    """
    Run the complete multi-agent supply chain monitoring pipeline.
    """

    orchestrator = SupplyChainOrchestrator()

    result = orchestrator.run()

    return result