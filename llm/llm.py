import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv(override=True)

# Retrieve API key
api_key_new = os.getenv("OPENAI_API_KEY")
if not api_key_new:
    raise ValueError("Error: OPENAI_API_KEY not found in .env file.")
print("API Key Loaded Successfully!",api_key_new)
print("API Key Loaded Successfully!")

# Retrieve model name with a default fallback
model_name = os.getenv("OPENAI_MODEL", "gpt-4")

async def get_chat_model():
    """Asynchronously initializes the ChatOpenAI model."""
    return ChatOpenAI(model=model_name)
