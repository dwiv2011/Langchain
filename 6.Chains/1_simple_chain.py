#step 1: asking prompt from user
#step 2:Invoking the LLM application
#Step 3:providng the result

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt=PromptTemplate(
        template='generate 5 interesting facts about {topic}',
        input_variables=['topic'])

model=ChatOpenAI()
#ideally, we do use model.invoke()
parser=StrOutputParser()
chain=prompt | model | parser

result=chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()

