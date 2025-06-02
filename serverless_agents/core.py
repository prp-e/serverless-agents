import os
from openai import OpenAI

client = OpenAI(
    base_url = os.environ['OPENAI_BASE_URL'],
    api_key = os.environ['OPENAI_API_KEY']
)