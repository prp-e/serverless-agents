import os
from openai import OpenAI

client = OpenAI(
    base_url = os.environ['OPENAI_BASE_URL'],
    api_key = os.environ['OPENAI_API_KEY']
)

class Agent:
    def __init__(self, model):
        self.model = model 
        self.system_message = '''
You are a helpful assistant which has access to the following tools. Your task is to just turn user's prompts into the needed input for each tool based on the description provided. 

Here is the list of the tools:
'''

    def tool(self, description):
        def decorator(func):
            tool = f"{func.__name__}: {list(func.__code__.co_varnames)} - {description}"
            self.system_message = self.system_message + "\n- " + tool

            return func
        return decorator
    
    def tool_calling(self):
        pass