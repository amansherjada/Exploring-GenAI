from phi.agent.agent import Agent
from phi.model.groq.groq import Groq
from phi.tools.yfinance import YFinanceTools # https://docs.phidata.com/tools/yfinance#yfinance
from dotenv import load_dotenv

load_dotenv()

agent =  Agent(
    name='groq',
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Use tables to display the stock price and analyst recommendations."],
)

agent.print_response("Summerize the stock price and analyst recommendations for Apple (AAPL) and Microsoft (MSFT). Provide a table with the stock price and analyst recommendations for each stock. Provide recommendations for each stock based on the stock price and analyst recommendations.")