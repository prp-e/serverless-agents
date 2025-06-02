import json
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
Your output MUST BE A JSON OBJECT like the following:

{"tool" : TOOL_NAME, "argument1" : ARGUMENT_1, ...}

Also remember, do not use markdown.

Here is the list of the tools:
'''
        self.tools = []

    def tool(self, description):
        def decorator(func):
            tool = f"{func.__name__}: {list(func.__code__.co_varnames)} - {description}"
            self.system_message = self.system_message + "\n- " + tool

            self.tools.append(func)

            return func
        return decorator
    
    def tool_preparation(self, message):
        
        result = client.chat.completions.create(
            model = self.model, 
            messages = [
                {
                    "role" : "system",
                    "content" : self.system_message
                },
                {
                    "role" : "user",
                    "content" : message
                }
            ],
            temperature = 0.0 
        )

        return result.choices[0].message.content
    
    def tool_calling(self, data):
        pass