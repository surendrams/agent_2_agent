# Agent2Agent Flight Booking Demo

A demonstration of Agent-to-Agent (A2A) communication using Google's Agent Development Kit (ADK) and the A2A SDK. This project implements a flight booking service with a remote agent (server) that provides flight search and booking capabilities, and a client agent that can interact with it.

## Overview

This project showcases how two AI agents can communicate using the A2A protocol:
- **Remote Agent (Server)**: A travel agent that provides flight search and booking tools
- **Client Agent**: Connects to the remote agent to access flight services

## Project Structure

```
agent_2_agent/
├── adk_a2a/
│   ├── client/
│   │   ├── agent.py          # Client agent that connects to remote service
│   │   └── .env              # Client environment configuration
│   └── remote/
│       ├── agent.py          # Server agent with flight tools
│       └── .env              # Server environment configuration
├── main.py                   # Entry point
├── pyproject.toml            # Project dependencies and metadata
├── uv.lock                   # Lock file for uv package manager
└── README.md                 # This file
```

## Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip
- Google API Key (for Gemini AI)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd agent_2_agent
```

2. Install dependencies using uv:
```bash
uv sync
```

Or using pip:
```bash
pip install -e .
```

## Configuration

### Environment Variables

Both the client and server require environment configuration. Create or update `.env` files in the respective directories:

**adk_a2a/client/.env** and **adk_a2a/remote/.env**:
```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Google API key for Gemini.

## Running the Application

### 1. Start the Remote Agent (Server)

The remote agent runs on port 8081 and provides flight search and booking services.

```bash
# Start the server
uvicorn adk_a2a.remote.agent:a2a_app --host localhost --port 8081
```

The server will start and expose the FlightBookingAgent at `http://localhost:8081`.

### 2. Start the Client Agent

In a new terminal, start the client agent that connects to the remote service:

```bash
# Navigate to the client agent directory
cd adk_a2a/client

# Start the client
uv run adk dev run agent.py
```

## Features

### Flight Search
The remote agent provides hardcoded flight search functionality with:
- Route: LAX to NYC
- Multiple flight options (American Airlines, United Airlines, Delta Airlines)
- Flight details including departure/arrival times, duration, price, and stops

### Flight Booking
Mock flight booking functionality that returns:
- Booking confirmation numbers
- Passenger details
- Seat assignments
- Meal preferences
- Baggage allowance
- Cancellation policy

## Architecture

The application uses:
- **Google ADK**: Agent Development Kit for building AI agents
- **A2A SDK**: Agent-to-Agent communication protocol
- **Gemini 2.0 Flash**: Google's AI model for agent intelligence
- **RemoteA2aAgent**: For client-server agent communication
- **LlmAgent**: For the server-side agent with tools

## Development

### Dependencies

Main dependencies (defined in `pyproject.toml`):
- `google-adk>=1.21.0` - Google Agent Development Kit
- `a2a-sdk>=0.3.0` - Agent-to-Agent SDK
- `python-dotenv>=1.0.0` - Environment variable management
- `uvicorn>=0.30.0` - ASGI server

### Package Manager

This project uses [uv](https://github.com/astral-sh/uv) for fast, reliable Python package management. The `uv.lock` file ensures reproducible installations.

## Security Notes

- Never commit `.env` files with real API keys to version control
- API keys are sensitive credentials and should be kept secure
- Consider using environment-specific configurations for production deployments

## Next Steps

- Implement dynamic flight search with real parameters
- Add error handling and validation
- Integrate with real flight APIs
- Add authentication and authorization
- Implement more sophisticated travel agent capabilities

## License

This project is for educational and demonstration purposes.
