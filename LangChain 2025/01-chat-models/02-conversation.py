from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Define the initial conversation messages
messages = [
    # System message to introduce the user's expertise
    SystemMessage("You are a Expert in Social Media Marketing"),
    # Human message to inquire about services
    HumanMessage("I want to know more about your services")
]
llm = ChatGroq(model="mixtral-8x7b-32768")

result = llm.invoke(messages)

print(result.content)