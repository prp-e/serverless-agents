import os 

os.environ['OPENAI_BASE_URL'] = "http://localhost:11434/v1"
os.environ['OPENAI_API_KEY'] = "ollama-doesnt-need-api-key"

from serverless_agents import Agent

agent = Agent("haghiri/xei:2b")

@agent.tool("This tool calculates the average of three numbers.")
def avg(a, b, c):
    sum = a + b + c
    return sum / 3.0

result = agent.chat("What is the average of 10, 13 and 20?")
print(result)