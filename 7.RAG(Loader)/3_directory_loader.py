from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4')

loader=DirectoryLoader(path="./books",glob="*.pdf",loader_cls=PyPDFLoader)
docs=loader.load()
#docs=loader.lazy_load() # if dealing with large files
print(len(docs))