from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    """Request model for endpoints that only need a prompt"""
    prompt: str = Field(..., description="The prompt for content generation", min_length=1)

class PromptContextRequest(BaseModel):
    """Request model for endpoints that need both prompt and context"""
    prompt: str = Field(..., description="The prompt for content generation", min_length=1)
    context: str = Field(..., description="Additional context for content generation", min_length=1)

class PPTRequest(BaseModel):
    """Request model for PowerPoint generation"""
    prompt: str = Field(..., description="The prompt for presentation content", min_length=1)
    context: str = Field(..., description="Additional context for the presentation", min_length=1)
    template: str | None = Field(
        None, 
        description="Optional template name (professional_blue, modern_green, vibrant_orange, elegant_purple, corporate_gray). If not provided, a random template will be used."
    )

class ContentResponse(BaseModel):
    """Response model for all content generation endpoints"""
    content: str = Field(..., description="The generated content")
    message: str = Field(default="Content generated successfully", description="Status message")
