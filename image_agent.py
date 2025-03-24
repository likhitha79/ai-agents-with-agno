from pathlib import Path
from agno.models.groq import Groq
from agno.agent import Agent
from agno.media import Image

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    agent_id="car-location-classifier",
    name="Car Location Classifier",
    markdown=True,
    debug_mode=True,
    show_tool_calls=True,
    instructions=[
        "You are an AI agent that classifies whether a car is in a driveway or a parking lot.",
        "Analyze the background, road type, and surrounding structures to determine the correct classification.",
        "Respond with either 'Driveway' or 'Parking Lot' along with a short explanation.",
    ],
)

image_path = "car_image.jpg"

agent.print_response(
    "Is the car in a driveway or a parking lot? Provide reasoning.",
    images=[Image(filepath=image_path)],
    stream=True,
)
