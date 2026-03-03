from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()

llm_used=HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.2-1B-Instruct",task="text-generation")
model= ChatHuggingFace(llm=llm_used)

result=model.invoke("what is the capital of india?")
print(result.content)