from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(model="gemma2-9b-it")

# Prompt with System and Human Messages (Using Tuples)
messages = [
    ("system","You are a comedian who tells jokes about {topic}."),
    ("human","Tell me {joke_counts} jokes.")
]

prompt_template = ChatPromptTemplate.from_messages(messages=messages)

prompt = prompt_template.invoke({"topic": "doctor", "joke_counts": 3})

print(prompt)

response = llm.invoke(prompt)

print(response.content)