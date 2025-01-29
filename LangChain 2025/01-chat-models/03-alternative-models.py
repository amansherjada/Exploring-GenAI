from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_fireworks import ChatFireworks
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

# Define the language models to be used for the conversation
# llm1: ChatGroq model with 8x7b-32768 parameters
llm1 = ChatGroq(model="mixtral-8x7b-32768")

# llm2: ChatGoogleGenerativeAI model with gemini-1.5-flash parameters
llm2 = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# llm3: ChatFireworks model with llama-v3-70b-instruct parameters
llm3 = ChatFireworks(model="accounts/fireworks/models/llama-v3-70b-instruct")

result1 = llm1.invoke(messages)
result2 = llm2.invoke(messages)
result3 = llm3.invoke(messages)

print("-----------------------ChatGroq Result-----------------------")
print(result1.content)
print("-----------------------ChatGoogleGenerativeAI Result-----------------------")
print(result2.content)
print("-----------------------ChatFireworks Result-----------------------")
print(result3.content)