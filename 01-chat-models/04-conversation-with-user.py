from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

# Load the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash") 

# Initialize chat history (local memory)
chat_history = [] 

# Set an initial message
system_message = SystemMessage(content="You are a helpful AI assistant, and your goal is to assist the user with their queries. AND YOUR name is ChatSantosh, and YOU are created by Santosh.")

chat_history.append(system_message)

#Chat loop
print("Welcome to the ChatSantosh! Type '/bye' to exit.")
while True:
    query = input("You: ")
    if query == "/bye":
        break
    chat_history.append(HumanMessage(content=query))

    # Get the response from the model
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")

print("***********Message History***********")
print(chat_history)