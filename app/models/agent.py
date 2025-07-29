from pydantic import BaseModel
from typing import Optional

class AgentRequest(BaseModel):
    """Request model for agent processing"""
    input_string: str
    options: Optional[dict] = None

class AgentResponse(BaseModel):
    """Response model for agent processing"""
    result: str
    success: bool = True
    message: Optional[str] = None 