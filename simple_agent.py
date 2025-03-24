from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

# Initialize the agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are an intelligent e-commerce assistant helping customers find products.",
    tools=[DuckDuckGoTools()],  
    show_tool_calls=True
)

agent.print_response("In which ecommerce platforms I can get Nike shoes", stream=True)
