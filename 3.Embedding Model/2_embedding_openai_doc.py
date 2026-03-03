from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
doc=["Delhi is capital of india","Lucknow is capital of Uttar pradesh","cricket is religion of india"]
embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
result= embedding.embed_documents(doc)
print(str(result))