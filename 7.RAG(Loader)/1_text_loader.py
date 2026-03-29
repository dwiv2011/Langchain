from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4')
prompt=PromptTemplate(template="summarize the {topic}",input_variables=['topic'])
loader=TextLoader('FastAPI_Complete_Guide_text.txt')
docs=loader.load()
# for i, doc in enumerate(docs):
#     print(f"\nDocument {i+1}")
#     print(f"Source: {doc.metadata}") # As the documents will have two things , metadata & Page_content
#     print(doc.page_content)


parser=StrOutputParser()

chain =prompt|model|parser
print(chain.invoke({'topic':docs[0].page_content}))
