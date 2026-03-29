from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model=ChatOpenAI(model='gpt-4')

prompt =PromptTemplate(template="Answer the {question} on basis of  {topic}",
                       input_variables=['question','topic'])

loader=WebBaseLoader("https://www.amazon.in/COOTER-30-Waterfall-Sink-Multifunctional/dp/B0DWSYJLCB/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.9lmXcbX0ToqYLVnGZm_6laymReuiKXFgu-bdZS5v4kbcVDBr2nR1ua_iuH7VOKfN3gjYH-1pZcqPqkLxF1xQpQkINCdXRsO61i0PvlBOfLbL_L8YqpkCrRAFG98fNhk5-Tr7sv1iOkwkSm-jB_facNfjJeKDomhkodtM2I7scVQ2XrS-z52mqz0swJeLSApdvYkhCGch-DbvKCauvKKbQay_iMVX3IFdwqHy6avUJ_4.02kuE9ZxELYzUg483wWR8NuzyLba7G6FlWFz4mr1bYA&dib_tag=se&qid=1774750933&refinements=p_89%3ACarysil&s=home-improvement&sr=1-1-spons&aref=F9WYtUiNA6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl&psc=1")

docs =loader.load()

parser=StrOutputParser()
# print(len(docs))

# print(docs[0].page_content)

chain=prompt|model|parser

out=chain.invoke({'question':"what is the size of the sink",'topic':docs[0].page_content})

print(out)

