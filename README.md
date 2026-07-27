# Weather AI Agent

## Overview
The Weather AI Agent is a Python-based intelligent assistant that provides real-time weather information using the OpenRouter API and an external weather service (Open-Meteo). The application is designed to answer only weather-related queries by utilizing AI function calling and live data retrieval instead of generating estimated responses.

The project demonstrates the implementation of AI agents, tool calling, prompt engineering, conversation memory, and API integration in Python.
<img width="1057" height="636" alt="image" src="https://github.com/user-attachments/assets/f4aed49a-ad7f-419a-91aa-e071530e02b4" />
## Features
- Real-time weather information retrieval
- Coordinate lookup for cities
- AI-powered responses using the OpenRouter API
- Function (Tool) Calling for live data retrieval
- Conversation memory using JSON
- Environment variable support for secure API key management
- Command-line interface for user interaction

## Technologies Used
- Python 3.x
- OpenRouter API
- Open-Meteo API
- Requests
- Python Dotenv
- JSON

## Project Structure
```text
Weather Agent/
│
├── main.py              # Main application
├── tools.py             # Weather tool functions
├── prompts.py           # AI system prompt
├── memory.py            # Conversation memory functions
├── memory.json          # Stores previous conversations
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables
└── README.md
```

## Installation

1. **Clone the repository** (if applicable) or navigate to the directory:
   ```bash
   cd "Weather Agent"
   ```

2. **Create a virtual environment (Optional)**
   - Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - Linux / macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the project directory:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

## Running the Application
```bash
python main.py
```

## Sample Interaction
```text
======================
 Weather AI Agent 
======================

You : What is the weather in London?

Agent :
Weather Report

City:
London

Temperature:
15.5 °C

Wind Speed:
12.0 km/h

Weather Code:
3
```

## How It Works
1. The user submits a weather-related query.
2. The AI agent sends the request to the OpenRouter language model.
3. If live weather information is required, the model invokes the appropriate tool (`get_weather`).
4. The tool retrieves the latest weather data from the external API (Open-Meteo).
5. The result is returned to the user.
6. Conversation history is stored locally for maintaining context.

## Supported Queries
Examples include:
- What is the weather in New York?
- Tell me the current temperature in Paris.
- What's the wind speed in Tokyo?
- Do I need an umbrella in London today?

## Dependencies
The project requires the following Python packages:
- `requests`
- `python-dotenv`

Install them using:
```bash
pip install -r requirements.txt
```

## Project Components
- **`main.py`**: Handles user interaction, communicates with the OpenRouter API, processes tool calls, and controls the agent workflow.
- **`tools.py`**: Provides functions for retrieving coordinates and weather data.
- **`prompts.py`**: Contains the system prompt that restricts the AI agent to weather-related tasks.
- **`memory.py`**: Implements persistent conversation storage using a JSON file.

## Future Enhancements
- Graphical User Interface (GUI)
- Web application using Flask or Streamlit
- Historical weather data analysis
- Multi-language support
- Forecast for multiple days
- Voice-enabled interaction

## Learning Outcomes
This project demonstrates practical implementation of:
- AI Agents
- Prompt Engineering
- Function Calling
- REST API Integration
- Environment Variable Management
- JSON Data Handling
- Conversation Memory
- Python Programming

## License
This project is developed for educational and learning purposes. It may be modified and extended for personal or academic use.

## Author
Varshika Saravanan

Bachelor of Technology – Information Technology
