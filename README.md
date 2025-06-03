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