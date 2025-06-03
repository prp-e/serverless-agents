import os 

base_url = "https://text.pollinations.ai/openai"
os.environ['OPENAI_BASE_URL'] = base_url
os.environ['OPENAI_API_KEY'] = "pollinations-do-not-need-a-key"

# Important: Always do this before the rest of the code since Agent object tries to override above environment variables.

from serverless_agents import Agent


agent = Agent("openai")

@agent.tool("This tool calculates the average of three numbers.")
def avg(a, b, c):
    sum = a + b + c
    return sum / 3.0

result = agent.chat("What is the average of 10, 13 and 20?")
print(result)