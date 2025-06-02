import json
import os
from openai import OpenAI

client = OpenAI(
    base_url = os.environ.get('OPENAI_BASE_URL', 'https://api.openai.com/v1'),
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
        data = json.loads(data)
        tool = data['tool']

        del data['tool']

        for t in self.tools:
            if t.__name__ == tool:
                called_tool = t
        
        data = data.values()
        result = called_tool(*data)

        return result
    
    def chat(self, message):
        
        prepared_tool = self.tool_preparation(message)
        results = self.tool_calling(prepared_tool)

        self.history = [
                {
                    "role" : "system",
                    "content" : '''You are a helpful assistant and you are fed with the results from a previous tool calling.
                    First, you have to show the users the JSON object of tool and its arguments. 
                    Then you show the user the resut. 
                    Then you provide an explanation to the user about what executed and why the result is like that.
                    '''
                },
            ]
        
        self.history.append({"role" : "user", "content" : f"Tool and arguments:{prepared_tool}\nResutls: {results}"})

        humanized_result = client.chat.completions.create(
            model = self.model, 
            messages = self.history,
            temperature = 0.5
        )

        chatbot_result = humanized_result.choices[0].message.content
        
        self.history.append({"role" : "assistant", "content" : chatbot_result})

        return chatbot_result