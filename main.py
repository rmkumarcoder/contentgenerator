from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from models import PromptRequest, PromptContextRequest, PPTRequest, ContentResponse
from openai_client import generate_content
from ppt_generator import create_presentation
import os

app = FastAPI(
    title="AI Content Generator API",
    description="API for generating various types of content using GenAI",
    version="1.0.0"
)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "AI Content Generator API",
        "version": "1.0.0",
        "endpoints": [
            "/blog-post",
            "/whitepaper",
            "/ppt",
            "/facebook-post",
            "/linkedin-post"
        ]
    }

@app.post("/blog-post", response_model=ContentResponse)
async def create_blog_post(request: PromptRequest):
    """
    Generate a blog post from a prompt.
    
    Takes a prompt and creates engaging blog content using AI.
    """
    try:
        system_message = """You are an expert blog writer. Create engaging, well-structured blog posts 
        with clear headings, compelling introductions, informative body content, and strong conclusions. 
        Use a conversational yet professional tone. Include relevant examples and insights."""
        
        content = generate_content(
            prompt=request.prompt,
            system_message=system_message,
            max_completion_tokens=8192
        )
        
        return ContentResponse(content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating blog post: {str(e)}")

@app.post("/whitepaper", response_model=ContentResponse)
async def create_whitepaper(request: PromptRequest):
    """
    Generate a whitepaper from a prompt.
    
    Takes a prompt and creates a professional, research-focused whitepaper.
    """
    try:
        system_message = """You are an expert technical writer specializing in whitepapers. 
        Create comprehensive, well-researched whitepapers with executive summaries, problem statements, 
        methodology, analysis, conclusions, and recommendations. Use formal, authoritative language 
        with proper citations and data-driven insights. Structure the content with clear sections."""
        
        content = generate_content(
            prompt=request.prompt,
            system_message=system_message,
            max_completion_tokens=8192
        )
        
        return ContentResponse(content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating whitepaper: {str(e)}")

@app.post("/ppt")
async def create_ppt(request: PPTRequest):
    """
    Generate an actual PowerPoint (.pptx) file from prompt and context.
    
    Takes a prompt, context, and optional template to create a downloadable presentation.
    
    Available templates:
    - professional_blue (default)
    - modern_green
    - vibrant_orange
    - elegant_purple
    - corporate_gray
    
    If no template is specified, a random template will be used.
    """
    try:
        filename = create_presentation(
            prompt=request.prompt,
            context=request.context,
            template_name=request.template
        )
        
        if not os.path.exists(filename):
            raise HTTPException(status_code=500, detail="Failed to generate presentation file")
        
        return FileResponse(
            path=filename,
            media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            filename=os.path.basename(filename),
            headers={
                "Content-Disposition": f"attachment; filename={os.path.basename(filename)}"
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating PowerPoint: {str(e)}")

@app.post("/facebook-post", response_model=ContentResponse)
async def create_facebook_post(request: PromptContextRequest):
    """
    Generate a Facebook post from prompt and context.
    
    Takes a prompt and context to create engaging social media content for Facebook.
    """
    try:
        system_message = """You are a social media expert specializing in Facebook content. 
        Create engaging, friendly Facebook posts that encourage interaction. Use emojis appropriately, 
        include a hook to grab attention, tell a story or share value, and include a clear call-to-action. 
        Keep it conversational and relatable. Suggest relevant hashtags at the end."""
        
        full_prompt = f"{request.prompt}\n\nContext: {request.context}"
        
        content = generate_content(
            prompt=full_prompt,
            system_message=system_message,
            max_completion_tokens=2048
        )
        
        return ContentResponse(content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating Facebook post: {str(e)}")

@app.post("/linkedin-post", response_model=ContentResponse)
async def create_linkedin_post(request: PromptContextRequest):
    """
    Generate a LinkedIn post from prompt and context.
    
    Takes a prompt and context to create professional content for LinkedIn.
    """
    try:
        system_message = """You are a professional content creator specializing in LinkedIn posts. 
        Create engaging, professional LinkedIn content that provides value to a business audience. 
        Use a professional yet personable tone, share insights or lessons, include relevant industry 
        knowledge, and end with a thought-provoking question or call-to-action to encourage engagement. 
        Use minimal emojis. Suggest relevant professional hashtags at the end."""
        
        full_prompt = f"{request.prompt}\n\nContext: {request.context}"
        
        content = generate_content(
            prompt=full_prompt,
            system_message=system_message,
            max_completion_tokens=2048
        )
        
        return ContentResponse(content=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating LinkedIn post: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
