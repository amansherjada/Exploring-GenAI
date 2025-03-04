from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Simple Agent",
    model = Groq(id= "llama-3.3-70b-versatile")

)

agent.print_response("Write a short story about a cat and a dog", stream=True)