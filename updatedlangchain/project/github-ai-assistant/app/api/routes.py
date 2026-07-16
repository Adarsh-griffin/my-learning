"""
API Routes

Expose the GitHub AI Agent through FastAPI.
"""

from fastapi import APIRouter, HTTPException

from app.models import ChatRequest, ChatResponse
from app.agents.github_agent import agent

router = APIRouter(
    prefix="/api",
    tags=["GitHub AI"],
)


@router.get("/")
def health_check():
    return {
        "status": "running",
        "service": "GitHub AI Assistant"
    }


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    try:

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": request.message,
                    }
                ]
            }
        )

        answer = response["messages"][-1].content

        return ChatResponse(
            answer=answer
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )