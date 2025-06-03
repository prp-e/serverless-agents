# Serverless Agents

_AI Agents_ are usually big and scary names at first glance. But they're basically LLM's on steriods which can use different tools. However, building an AI agent is always a challenge and I faced this challenge a lot. 

I personally used [n8n](https://n8n.io) and it was cool but I needed something more programmatical which can help me build even cooler stuff using AI models. Also I always had in mind that what happens if the model does not support _tool calling_ natively? This tool is my answer to that. 

The whole idea of this tool comes from [Flask](https://flask.palletsprojects.com/en/stable/)'s `@app` decorator which adds routes to your web app or API. You just need to add a `tool` to your agent and you're good to go!

## Installation 

Currently, you can install this library like this: 

```bash
pip3 install git+https://github.com/prp-e/serverless-agents 
``` 

And this library will soon be added to [pypi](https://pypi.python.org) as well.

## Basic environment setup

The library needs two _environment variables_ to be set: 

* `OPENAI_BASE_URL` : If not set, it'll be set on default OpenAI's API endpoint. Otherwise, it'll be what you have set. 
* `OPENAI_API_KEY` : This is the API key you have. For providers such as OpenAI, Cloudflare (if using OpenAI compatible endpoints) or Open Router, this must be set. 

## Make a simple agent

In order to make a very simple agent, you can do this: 

```python
from serverless_agents import Agent

agent = Agent("gpt-4.1-nano")

@agent.tool("This tool is for saying Hi to people")
def greet(name):
    return f"Hello, {name}"

agent.chat("I just want to greet Samin")
``` 

The output of the above code will be something like this: 

```markdown
Here is the JSON object of the tool and its arguments:

\```json
{
  "tool": "greet",
  "name": "Samin"
}
\```

And here are the results from the tool call:
\```
Hello, Samin
\```

### Explanation

The tool used in this interaction is named `greet`, and it takes a single argument, `name`. In this case, the name provided was `"Samin"`.

When the `greet` tool is called with the argument `"Samin"`, it generates a greeting message. The output "Hello, Samin" is a standard greeting in English that acknowledges the presence of the person named Samin.

This tool is useful for creating personalized greetings, which can be used in various applications such as customer service, social media interactions, or any scenario where a friendly and personal touch is desired.
``` 

This way, you can make different stuff with _agentic_ behavior. 

## Contribution 

The contribution guide will be availabl as soon as possible. 

## Donations 

### Fiat Donation 

Currently there is no fiat option available (and I try my best to make it available). 

### Crypto Donation 

* BTC : `bc1qtah5agu8629kj3j3jx4w6w0nj7l4srknwg8wku`
* ETH (ETH, USDT, USDC) : `0x26abcBd0437C2F2B713D6C2d598cD4988DbacC87`
* TON : `UQBtQ4UBf1gOnlAfkgAo-XNNOCQ_dKlVWj3xygit7oUX4uVA`
* TRX (TRX, USDT) : `TKx8FWAozZmwDsPAYcGbNnE56mJDxJ4ZWF`
* SOL : `8VgLEL2Y6TFWgzdeK5zCMTRN23EQ4HZaK3xsoe6Jggnc`
* DOGE: `D7dG7Tk4C8e4K5UdPZyoU76tXZ5LkcCVm1`