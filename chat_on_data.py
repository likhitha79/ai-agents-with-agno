import pandas as pd
from pathlib import Path
from agno.agent import Agent
from agno.tools.csv_toolkit import CsvTools
from agno.models.groq import Groq
from agno.tools.pandas import PandasTools
from dotenv import load_dotenv


load_dotenv()
csv_path = "reviews_data.csv"


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[CsvTools(csvs=[csv_path]), PandasTools()],
    show_tool_calls=True,
    markdown=True,
    instructions=[
    "First always get the list of files",
        "Then check the columns in the file",
        "Then run the query to answer the question",
    ],
)


agent.print_response(" What is the average rating across the products?.", stream=True)

