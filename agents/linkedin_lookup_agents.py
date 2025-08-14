import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub



def lookup(name:str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    return "www.linkedin.com/in/hashamjavedofficial"
