from agno.agent import Agent
from agno.team import Team
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

# Web Agent: Finds product details & reviews
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    instructions=["Fetch product details, availability, and reviews from trusted sources. Always include links."],
    show_tool_calls=True,
    markdown=True
)

# Price Tracker Agent: Compares prices across e-commerce sites
price_tracker_agent = Agent(
    name="Price Tracker Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    instructions=["Compare product prices across Amazon, Flipkart, and Walmart. Always return results in a structured table with links."],
    show_tool_calls=True,
    markdown=True
)

# Customer Support Agent: Provides return & shipping policies
customer_support_agent = Agent(
    name="Customer Support Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],  
    instructions=["Find return policies, shipping estimates, and order tracking information for given products."],
    show_tool_calls=True,
    markdown=True
)

#**E-commerce Agent Team** (Collaboration Mode)
ecommerce_team = Team(
    name="E-Commerce Assistant",
    model=Groq(id="llama-3.3-70b-versatile"),
    members=[web_agent, price_tracker_agent, customer_support_agent],
    mode="coordinate",  # Agents work together to answer different parts of the query
    instructions=[
        "Delegate queries to the relevant agent.",
        "Ensure structured responses with sources.",
        "Use tables where needed (e.g., for price comparisons)."
    ],
    show_tool_calls=True,
    markdown=True,
    show_members_responses=True
)


response = ecommerce_team.run(
    "Find me a white Nike running shoe under $100, compare prices across Amazon and Flipkart, and check return policies."
).content

print(response)
