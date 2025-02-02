from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(model="gemma2-9b-it")

template = "Write a {tone} email to {company} expressing interest in {position} position, mentioning {skill} as a key strength. Keep it concise and to the point."

prompt_template = ChatPromptTemplate.from_template(template=template)

prompt = prompt_template.invoke({
    "tone": "formal",
    "company": "Google",
    "position": "Software Engineer",
    "skill": "Python"
})

# print(prompt)

response = llm.invoke(prompt)

print(response.content)