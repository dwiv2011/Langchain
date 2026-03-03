from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm_used=HuggingFacePipeline.from_model_id(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation")
model= ChatHuggingFace(llm=llm_used)
result=model.invoke("what is capital of india?")
print(result.content)