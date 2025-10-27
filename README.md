# AI Content Generator API

A FastAPI application that provides AI-powered content generation endpoints for various content types including blog posts, whitepapers, presentations, and social media posts.

## Features

- **Blog Post Creator**: Generate engaging blog posts from a prompt
- **Whitepaper Creator**: Create professional, research-focused whitepapers
- **PowerPoint Creator**: Generate structured presentation content with slides
- **Facebook Post Creator**: Create engaging social media content for Facebook
- **LinkedIn Post Creator**: Generate professional content for LinkedIn

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **OpenAI GPT-5**: Latest AI model for content generation (via Replit AI Integrations)
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running the application

## Setup

The application is already configured and running. It uses Replit AI Integrations for OpenAI access, which means:
- No personal API key required
- Charges are billed to your Replit credits
- Automatic key management and rotation

## API Endpoints

### Root Endpoint
```
GET /
```
Returns API information and available endpoints.

### Blog Post Creator
```
POST /blog-post
Content-Type: application/json

{
  "prompt": "Your blog post topic or description"
}
```

### Whitepaper Creator
```
POST /whitepaper
Content-Type: application/json

{
  "prompt": "Your whitepaper topic or description"
}
```

### PowerPoint Creator
```
POST /ppt
Content-Type: application/json

{
  "prompt": "Your presentation topic",
  "context": "Additional context or specific requirements"
}
```

### Facebook Post Creator
```
POST /facebook-post
Content-Type: application/json

{
  "prompt": "What you want to post about",
  "context": "Additional context or background information"
}
```

### LinkedIn Post Creator
```
POST /linkedin-post
Content-Type: application/json

{
  "prompt": "What you want to post about",
  "context": "Additional context or background information"
}
```

## Response Format

All endpoints return a JSON response with the following structure:

```json
{
  "content": "Generated content here...",
  "message": "Content generated successfully"
}
```

## Example Usage

### Using cURL

**Blog Post:**
```bash
curl -X POST "http://localhost:5000/blog-post" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write about the benefits of AI in healthcare"}'
```

**Facebook Post:**
```bash
curl -X POST "http://localhost:5000/facebook-post" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Promote a new product launch", "context": "Eco-friendly water bottle"}'
```

### Using Python

```python
import requests

# Blog post example
response = requests.post(
    "http://localhost:5000/blog-post",
    json={"prompt": "The future of renewable energy"}
)
result = response.json()
print(result["content"])

# LinkedIn post example
response = requests.post(
    "http://localhost:5000/linkedin-post",
    json={
        "prompt": "Share insights about remote work",
        "context": "Based on 2 years of experience managing a distributed team"
    }
)
result = response.json()
print(result["content"])
```

## Interactive API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: Visit `/docs` for interactive API testing
- **ReDoc**: Visit `/redoc` for alternative documentation

## Error Handling

If an error occurs during content generation, the API will return a 500 status code with error details:

```json
{
  "detail": "Error generating content: [error message]"
}
```

## Development

The application is configured to run on `0.0.0.0:5000`. The FastAPI server automatically reloads when code changes are detected.

## Project Structure

```
.
├── main.py              # FastAPI application and endpoints
├── models.py            # Pydantic request/response models
├── openai_client.py     # OpenAI client and content generation logic
├── README.md            # This file
└── .gitignore          # Git ignore configuration
```

## Notes

- Content generation may take several seconds depending on the complexity of the request
- The AI model (GPT-5) is optimized for high-quality output
- All endpoints support CORS for cross-origin requests
