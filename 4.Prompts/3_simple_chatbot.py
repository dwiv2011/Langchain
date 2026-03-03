from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4')
# without chathistory chat model can not recall the past conversation
chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ",result.content)

print(chat_history)

"""
below is output however when chat history prolonges then it fails to understand what was user prompt and what was AI Prompt

['Hi', 'Hello! How can I assist you today?', 'what is 2+5', '2 + 5 equals 7.', 'multiply by 4', 'The result of 7 multiplied by 4 is 28.', 'exit']
solution: 
1) use dictionary and use "User" or "AI" as keyword
2) use langchain provided solution
"""