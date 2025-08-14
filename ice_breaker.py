from dotenv import load_dotenv;
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
import os

from agents.linkedin_lookup_agents import lookup as lookup_linkedin_agent
from third_parties.linkedin import scrape_linkedin_profile

from output_parsers import summary_parser

load_dotenv()



def generate_linkedin_data(name:str) -> str:
    print('Hello World')
    print(__name__)
    linkedin_profile_url = lookup_linkedin_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url, mock=True)


    summary_template = """
         given the Linkedin information {information} about a person I want you to create:
         1. A short summary
         2. two interesting facts about them
         
         \n{format_instructions}
         """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template, partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        }
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, max_retries=2)

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": linkedin_data})

    print("res:", res)

if __name__ == '__main__':
    print(__name__)

    generate_linkedin_data(name="Hasham Javed Systems")