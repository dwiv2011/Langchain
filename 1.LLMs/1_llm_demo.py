from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model="gpt-3.5-turbo-instruct")
result= llm.invoke("what is the capital of india")
result2= llm.invoke("what is the 28/4")

print(result,result2,sep=":")