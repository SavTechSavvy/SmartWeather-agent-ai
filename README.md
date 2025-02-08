WeatherSense AI
Abstract
WeatherSense AI is a comprehensive weather prediction and analysis system powered by Azure AI. The project utilizes a suite of Azure AI agents, including custom models, to process and fetch real-time weather data, perform sentiment analysis, and generate health and safety alerts based on weather conditions. With the integration of Azure’s Text Analytics API, WeatherSense AI evaluates the sentiment of weather descriptions, providing users with meaningful insights about the atmosphere, while also ensuring their safety through health advisories.

Key Features:
Real-Time Weather Forecasting: Fetch current weather data and 5-day forecasts from OpenWeatherMap API.
Sentiment Analysis: Use Azure AI Text Analytics to perform sentiment analysis on weather descriptions, providing personalized emotional feedback.
Health & Safety Alerts: Generate tailored health advisories based on real-time weather data, such as extreme heat or freezing temperatures.
AI Agents: The project leverages Azure AI agents, like "weather-fetcher" and "data-processor," to handle data processing and weather predictions.
Gradio Interface: A user-friendly web interface where users can input location and email to receive detailed weather reports and visual forecasts.
Technologies Used:
Azure AI (Text Analytics and Custom Agents)
OpenWeatherMap API
Gradio (for interactive UI)
Matplotlib (for data visualization)
Email Sending (SMTP)
Setup and Usage:
Clone the repository:

bash
Copy
Edit
git clone https://github.com/username/WeatherSense-AI.git
Install required dependencies:

nginx
Copy
Edit
pip install -r requirements.txt
Set up the Azure credentials and OpenWeatherMap API key in the .env file.

Run the application:

nginx
Copy
Edit
python weather_interface.py
Access the Gradio interface via the provided URL to interact with the system.

AI Agents:
Weather Fetcher: An agent that gathers real-time weather data from OpenWeatherMap using the provided location (zip code or city name).
Data Processor: A data processing agent responsible for formatting and analyzing the data collected.
Sentiment Analyzer: This agent performs sentiment analysis on weather descriptions using Azure AI’s Text Analytics API, offering insights on whether the day feels positive, neutral, or negative.
Health & Safety Alerts:
The project includes AI-driven health advisories tailored to the weather conditions. For example, extreme heat will trigger warnings to stay hydrated, while freezing temperatures will recommend dressing warmly.
