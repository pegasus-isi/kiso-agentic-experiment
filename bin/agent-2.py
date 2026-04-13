#!/usr/bin/env python3

from pydantic import BaseModel

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider


class PresidentList(BaseModel):
    presidents: list[str]


ollama_model = OpenAIChatModel(
    model_name="gpt-oss:20b",
    provider=OllamaProvider(base_url="http://ollama:11434/v1"),
)
agent = Agent(ollama_model, output_type=PresidentList)

result = agent.run_sync("List the first five presidents of the United States")
print(result.output)
# > presidents=['George Washington', 'John Adams', 'Thomas Jefferson', 'James Madison', 'James Monroe']
print(result.usage())
# > RunUsage(input_tokens=131, output_tokens=167, requests=1)
