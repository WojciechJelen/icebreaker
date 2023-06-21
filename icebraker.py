import os
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup

load_dotenv()

if __name__ == "__main__":
    linkedin_profile_url = lookup(name="Eden Marco")
    print(linkedin_profile_url)
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    # summary_template = """
    #     given the Linkedin information {information} about the person from, I want you to create:
    #     1. a short summary of the person's life
    #     2. two interesting facts about the person
    # """

    # summary_prompt_template = PromptTemplate(
    #     template=summary_template,
    #     input_variables=["information"],
    # )

    # llm = ChatOpenAI(
    #     # langchain is gettign the api key from the environment for us
    #     # openai_api_key=os.environ["OPENAI_API_KEY"],
    #     temperature=0,
    #     model_name="gpt-3.5-turbo",
    # )

    # chain = LLMChain(
    #     llm=llm,
    #     prompt=summary_prompt_template,
    # )

    # print(chain.run(information=linkedin_data))
