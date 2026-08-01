from fastapi import APIRouter

from app.ai_gateway.gateway import AIGateway

router = APIRouter()

gateway = AIGateway()


@router.post("/chat")
def chat(prompt: str):
    """
    Envia um prompt ao AI Gateway.
    """
    response = gateway.generate(prompt)

    return {
        "response": response
    }