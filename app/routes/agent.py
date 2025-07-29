from fastapi import APIRouter, HTTPException
from app.models.agent import AgentRequest, AgentResponse
from app.services.agent import AgentService

router = APIRouter(prefix="/agent", tags=["agent"])

@router.post("/", response_model=AgentResponse)
async def process_string(request: AgentRequest):
    try:
        # Call the service function to process the string
        result = AgentService.process_string(request.input_string)
        
        return AgentResponse(
            result=result,
            success=True,
            message="String processed successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing string: {str(e)}"
        )