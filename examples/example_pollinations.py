from serverless_agents import Agent
import os 

base_url = "https://text.pollinations.ai/openai"
os.environ['OPENAI_BASE_URL'] = base_url

agent = Agent("openai")

@agent.tool("This tool calculates the average of three numbers.")
def avg(a, b, c):
    sum = a + b + c
    return sum / 3.0