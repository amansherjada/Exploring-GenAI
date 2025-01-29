from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from a .env file
load_dotenv()

# Initialize a ChatGroq object with the "mixtral-8x7b-32768" model
llm = ChatGroq(model="mixtral-8x7b-32768")

# Use the invoke method of the ChatGroq object to send a message
# to the AI model and get a response
result = llm.invoke("Hello, Who are you?")

# Print everything of the response from the AI model
# print(result)

# Print the content of the response from the AI model
print(result.content)