import os
from pathlib import Path
from dotenv import load_dotenv
from ice.recipe import recipe

# Load environment variables from .env file
load_dotenv(Path(__file__).parent / '.env')

# Now you can access the API key like this:
api_key = os.getenv('OPENAI_API_KEY')

async def say_hello():
    hola = await say_hola()
    return f"Hello world! {hola}"

async def say_hola():
    return "Hola mundo!"

recipe.main(say_hello)
