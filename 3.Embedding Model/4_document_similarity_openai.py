from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import dotenv;
dotenv.load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

doc=["Virat Kohli is great indian cricketer",
     "Roger Federer is GOAT of tennis",
     "Messy is king of soccer",
     "Jasprit Bumrah is a great bowler"]


#qury="Tell me about soccer"
qury="Tell me about FIFA"

doc_em=embedding.embed_documents(doc)
query=embedding.embed_query(qury)

result=cosine_similarity([query],doc_em)
print(result)


