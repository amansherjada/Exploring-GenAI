from phi.agent.agent import Agent
from phi.model.groq.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.googlesearch import GoogleSearch
# from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

groq_model = Groq(id="llama-3.3-70b-versatile")

web_agent = Agent(
    name="Web Agent",
    model=groq_model, 
    tools=[GoogleSearch()],
    instructions=["Always include Sources"],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=groq_model,
    tools=[YFinanceTools(stock_price=True, stock_fundamentals=True, company_info=True, analyst_recommendations=True)],
    instructions=["Use tables to display answer"],
    show_tool_calls=True,
    markdown=True
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=groq_model,
    instructions=["Always include Sources", "Use tables to display answer"],
    show_tool_calls=True,
    markdown=True
)

agent_team.print_response("Provide a summary of the latest analyst recommendations for NVDA, including target prices, ratings (buy/sell/hold), and key justifications. Additionally, gather and summarize the most recent news articles related to NVDA, ensuring to include sources and relevant financial insights. Display any numerical data in a structured table format", stream=True)