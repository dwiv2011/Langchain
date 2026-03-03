from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4')
#temperature: it ranges between 0 to 2 , higher the value so more randomness

result= model.invoke("what is the capital of india")
result2= model.invoke("what is the 28/4") # it was hallucinating in base LLM model

#print(result,result2,sep=":")  this will provide the entire information token, model, context window etc unlike llm model
print(result.content,result2.content,sep=":") 