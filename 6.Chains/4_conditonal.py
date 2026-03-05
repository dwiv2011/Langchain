
# we are providing the feedback and according to feedback ,it will trigger response either Positive or Negative
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model1=ChatOpenAI()

llm_used=HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.2-1B-Instruct",task="text-generation")
model2= ChatHuggingFace(llm=llm_used)


prompt1 =PromptTemplate(template='classify the reviews either positive or Negative \n {review}',
                        input_variables=['review'])

parser=StrOutputParser()
classiefier_chain=prompt1|model1|parser

result=classiefier_chain.invoke({'review':'Movie was awesome, . Acting was at top notch'})
# As above one may not classify into positive or negative always so to force it classify in two we need to use pydantic Parser


class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt2 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {review} \n {format_instruction}',
    input_variables=['review'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain2 = prompt2 | model1 | parser2
result2=classifier_chain2.invoke({'review': 'Movie was just OK'})
print(result2)
