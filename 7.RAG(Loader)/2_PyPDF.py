from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4')

loader=PyPDFLoader('Data Science Interview Questions.pdf')
docs=loader.load()
for i, doc in enumerate(docs):# in PDF loader every PDF page will be considered as a doc
    print(f"\nDocument {i+1}")
    print(f"Source: {doc.metadata}") # As the documents will have two things , metadata & Page_content
    print(doc.page_content)


