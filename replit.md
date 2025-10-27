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
├── main.py              # FastAPI application with all endpoints
├── models.py            # Pydantic models for request/response validation
├── openai_client.py     # OpenAI client configuration and content generation
├── test_api.py          # Test suite for all endpoints
├── README.md            # User-facing documentation
├── replit.md            # This file - project documentation
└── .gitignore          # Git ignore configuration
```

### Key Components

**main.py**
- FastAPI application instance
- Five POST endpoints for content generation
- CORS middleware configuration
- Error handling for API failures

**models.py**
- `PromptRequest`: For endpoints requiring only a prompt (blog, whitepaper)
- `PromptContextRequest`: For endpoints requiring prompt + context (ppt, social media)
- `ContentResponse`: Standard response format for all endpoints

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
