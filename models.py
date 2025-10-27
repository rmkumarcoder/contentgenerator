from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    """Request model for endpoints that only need a prompt"""
    prompt: str = Field(..., description="The prompt for content generation", min_length=1)

class PromptContextRequest(BaseModel):
    """Request model for endpoints that need both prompt and context"""
    prompt: str = Field(..., description="The prompt for content generation", min_length=1)
    context: str = Field(..., description="Additional context for content generation", min_length=1)

class ContentResponse(BaseModel):
    """Response model for all content generation endpoints"""
    content: str = Field(..., description="The generated content")
    message: str = Field(default="Content generated successfully", description="Status message")
