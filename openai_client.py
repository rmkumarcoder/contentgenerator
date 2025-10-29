import os
from openai import OpenAI

# Load .env file for local development
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not installed, environment variables should be set manually

# Check if running on Replit (with AI Integrations) or locally
AI_INTEGRATIONS_OPENAI_API_KEY = os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY")
AI_INTEGRATIONS_OPENAI_BASE_URL = os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL")
STANDARD_OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Determine which environment we're in
if AI_INTEGRATIONS_OPENAI_API_KEY and AI_INTEGRATIONS_OPENAI_BASE_URL:
    # Running on Replit with AI Integrations
    client = OpenAI(
        api_key=AI_INTEGRATIONS_OPENAI_API_KEY,
        base_url=AI_INTEGRATIONS_OPENAI_BASE_URL
    )
    DEFAULT_MODEL = "gpt-5"  # Replit AI Integrations supports gpt-5
    print("Using Replit AI Integrations")
elif STANDARD_OPENAI_API_KEY:
    # Running locally with standard OpenAI
    client = OpenAI(api_key=STANDARD_OPENAI_API_KEY)
    DEFAULT_MODEL = "gpt-4o"  # Standard OpenAI - use gpt-4o, gpt-4, or gpt-3.5-turbo
    print("Using standard OpenAI API")
else:
    raise ValueError(
        "No OpenAI API key found. Please set OPENAI_API_KEY in your .env file "
        "or environment variables."
    )

def generate_content(prompt: str, system_message: str, max_completion_tokens: int = 8192) -> str:
    """
    Generate content using OpenAI's language model.
    
    Automatically uses gpt-5 on Replit or gpt-4o locally.
    
    Args:
        prompt: User's prompt/request
        system_message: System instruction for the AI
        max_completion_tokens: Maximum tokens in the completion
        
    Returns:
        Generated content as string
    """
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        max_completion_tokens=max_completion_tokens
    )
    
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("No content generated from the API")
    return content
