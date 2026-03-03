from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

result=embedding.embed_query("New delhi is capital of india")

print(str(result))