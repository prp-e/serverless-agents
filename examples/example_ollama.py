import os 

os.environ['OPENAI_BASE_URL'] = "http://localhost:11434/api/v1"
os.environ['OPENAI_API_KEY'] = "ollama-doesnt-need-api-key"

from serverless_agents import Agent

agent = Agent("haghiri/xei:2b")
