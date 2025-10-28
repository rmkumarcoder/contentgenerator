# AI Content Generator API - Project Documentation

## Overview
A FastAPI-based REST API that provides AI-powered content generation for various content types including blog posts, whitepapers, presentations, and social media posts. The application uses OpenAI's GPT-5 model via Replit AI Integrations.

## Current State
The application is fully functional with all five endpoints implemented and tested:
- Blog post creator (POST /blog-post)
- Whitepaper creator (POST /whitepaper)
- PowerPoint creator (POST /ppt)
- Facebook post creator (POST /facebook-post)
- LinkedIn post creator (POST /linkedin-post)

## Recent Changes
- **2025-10-28**: Enhanced PowerPoint generation
  - Implemented actual .pptx file generation using python-pptx library
  - Added 5 customizable presentation templates (professional_blue, modern_green, vibrant_orange, elegant_purple, corporate_gray)
  - Optional template parameter - random template used if not specified
  - Added fallback mechanism for AI generation failures
  - Updated /ppt endpoint to return downloadable .pptx files instead of JSON
  - Added comprehensive error handling and validation
  
- **2025-10-27**: Initial project setup
  - Created FastAPI application with five content generation endpoints
  - Integrated OpenAI GPT-5 via Replit AI Integrations
  - Implemented Pydantic models for request/response validation
  - Added CORS middleware for cross-origin support
  - Created comprehensive documentation and test suite
  - Configured workflow to run FastAPI server on port 5000

## Project Architecture

### File Structure
```
.
├── main.py                # FastAPI application with all endpoints
├── models.py              # Pydantic models for request/response validation
├── openai_client.py       # OpenAI client configuration and content generation
├── ppt_generator.py       # PowerPoint generation logic with templates
├── test_api.py            # Test suite for text content endpoints
├── test_ppt_endpoint.py   # Test suite for PowerPoint endpoint
├── README.md              # User-facing documentation
├── replit.md              # This file - project documentation
├── .gitignore             # Git ignore configuration
└── generated_ppts/        # Generated PowerPoint files (gitignored)
```

### Key Components

**main.py**
- FastAPI application instance
- Five POST endpoints for content generation
- CORS middleware configuration
- Error handling for API failures

**models.py**
- `PromptRequest`: For endpoints requiring only a prompt (blog, whitepaper)
- `PromptContextRequest`: For endpoints requiring prompt + context (social media)
- `PPTRequest`: For PowerPoint endpoint with optional template parameter
- `ContentResponse`: Standard response format for text content endpoints

**ppt_generator.py**
- `create_presentation()`: Main function to generate .pptx files
- `parse_ai_slides()`: Parse AI-generated content into structured slides with validation
- `create_fallback_slides()`: Fallback content when AI generation fails
- `get_template()`: Select template by name or return random template
- 5 predefined color templates for professional presentations

**openai_client.py**
- OpenAI client initialization using Replit AI Integrations
- `generate_content()`: Core function for AI content generation
- Uses GPT-5 model with configurable token limits

## Technology Stack
- **Language**: Python 3.11
- **Framework**: FastAPI
- **Server**: Uvicorn
- **AI Model**: OpenAI GPT-5 (via Replit AI Integrations)
- **Validation**: Pydantic
- **Package Manager**: uv

## Dependencies
- fastapi
- uvicorn[standard]
- openai
- python-pptx
- pydantic (included with FastAPI)

## Configuration

### Environment Variables
Automatically managed by Replit AI Integrations:
- `AI_INTEGRATIONS_OPENAI_API_KEY`: Authentication key (auto-managed)
- `AI_INTEGRATIONS_OPENAI_BASE_URL`: API endpoint (auto-managed)

### Workflow
- **Name**: FastAPI Server
- **Command**: `uvicorn main:app --host 0.0.0.0 --port 5000`
- **Port**: 5000
- **Output**: Webview

## User Preferences
No specific user preferences documented yet.

## Usage Notes
- Content generation can take 10-30 seconds depending on complexity
- API uses OpenAI GPT-5, charges billed to Replit credits
- No personal API key required
- All endpoints return JSON with `content` and `message` fields
- Interactive API docs available at `/docs` and `/redoc`

## Testing
Run the test suite with:
```bash
python test_api.py
```

Or test individual endpoints with curl:
```bash
curl -X POST "http://localhost:5000/blog-post" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Your topic here"}'
```

## Next Steps (Future Enhancements)
- Add file download endpoints for PPT generation (actual .pptx files)
- Implement content length customization parameters
- Add tone and style options (professional, casual, technical)
- Create rate limiting and usage tracking
- Add content caching to reduce duplicate AI generation costs
