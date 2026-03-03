from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated

load_dotenv()
model=ChatOpenAI()

#schema
class Review(TypedDict):
    # Annotated has added so it prompt should not get confuse with summary with other summary
    summary: Annotated[str, "A brief of reviews"] 
    sentiment:str

# below is additional steps
structured_model =model.with_structured_output(Review)
#

result = structured_model.invoke("""Located near ORR, have to walk inside a private property. Major house type are of 2bhks. JV project and not CREDAI certified/listed builder. Average cost of "1" apartment in this building is 70+L without registration. Has basic amenities of car parking/club house and a pool built over a basement of parking.

Opinion: The cost to value proposition of apartment is low. Many units are 2bhks very much suitable for renting out and will have a moving crowd , so will have hassle of active maintenance of society. Open private land around so good chance newer/bigger apartment will raise around.""")

print(result)
print(result['summary'])
print(result['sentiment'])