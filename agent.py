import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from deepagents import create_deep_agent

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key,
    temperature=0
)

agent = create_deep_agent(
    model=llm,
    tools=[],
    system_prompt="""
You are a helpful Deep AI Agent.
Always think step by step before answering.
"""
)