from google.adk.agents.remote_a2a_agent import RemoteA2aAgent, AGENT_CARD_WELL_KNOWN_PATH
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

root_agent = RemoteA2aAgent(
    name ="FlightBookingAgent",
    description = "An agent that can search and book flights using a remote flight booking service.",
    agent_card = f"http://localhost:8081/{AGENT_CARD_WELL_KNOWN_PATH}"
)
