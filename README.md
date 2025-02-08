# SmartWeather AI Agent

## Abstract

**SmartWeather AI Agent** is a comprehensive, AI-powered weather reporting system that leverages Azure AI agents and OpenAI models to provide real-time weather data, sentiment analysis, and health and safety alerts. By integrating OpenWeatherMap for live weather information with Azure AI Services for natural language and sentiment processing, SmartWeather AI delivers personalized weather insights, actionable advisories, and detailed forecasts via an interactive web interface and email notifications.

---

## Key Features

- **Real-Time Weather Forecasting:**  
  Retrieves current weather conditions and a 5-day forecast using the OpenWeatherMap API.

- **Sentiment Analysis:**  
  Analyzes the sentiment of weather descriptions using Azure's Text Analytics (powered by Azure OpenAI models) to offer personalized emotional insights (e.g., "The weather is great! You should feel happy and energetic").

- **Health & Safety Alerts:**  
  Generates health advisories based on extreme weather conditions (e.g., extreme heat, freezing temperatures, or high humidity) to help users take precautionary measures.

- **AI Agent Orchestration:**  
  Utilizes multiple Azure AI agents for data processing, sentiment analysis, and alert generation, all coordinated by a Comprehensive Weather Agent.

- **Interactive User Interface:**  
  A Gradio-powered web interface allows users to input their location and email to receive detailed weather reports and visual forecast graphs.

- **Email Reporting:**  
  Sends formatted HTML email reports that include current weather, a 5-day forecast, sentiment analysis, and health & safety alerts.

---

## Technologies Used

- **Azure AI Agents:**  
  Leverages Azure AI agents (including OpenAI models) to perform data processing, sentiment analysis, and generate insights.

- **Azure Foundry Project Connection String:**  
  Manages agent orchestration and integration using Azure Foundry's project connection string.

- **OpenWeatherMap API:**  
  Provides real-time weather data and forecasts.

- **Azure AI Services (Text Analytics):**  
  Processes and analyzes textual data for sentiment analysis.

- **Python:**  
  Primary programming language used to implement the system logic and API interactions.

- **Gradio:**  
  Builds a user-friendly web interface for interacting with the weather agent.

- **Matplotlib:**  
  Generates graphical visualizations (e.g., line charts for forecast data).

- **SMTP & MIME:**  
  Sends detailed HTML email reports with weather insights.

---

## AI Agents in WeatherSense AI

### 1. Weather Fetcher Agent
- **Task:**  
  Fetches real-time weather data and 5-day forecasts for a specified location (city or zip code) from the OpenWeatherMap API.
- **Key Function:**  
  Retrieves temperature, weather condition, humidity, and wind speed data.

### 2. Data Processor Agent
- **Task:**  
  Processes and formats raw weather data into user-friendly output for display and email reporting.
- **Key Function:**  
  Structures the weather forecast data into readable formats (HTML for email and graphical reports).

### 3. Sentiment Analyzer Agent
- **Task:**  
  Uses Azure AI Services (Text Analytics API) to analyze the sentiment of weather descriptions (e.g., "overcast clouds") and determine the emotional tone (positive, neutral, or negative).
- **Key Function:**  
  Provides personalized feedback based on weather sentiment (e.g., "😊 The weather is great! You should feel happy and energetic").

### 4. Health & Safety Alerts Agent
- **Task:**  
  Evaluates the weather conditions to generate health and safety advisories based on temperature and humidity thresholds.
- **Key Function:**  
  Issues warnings for extreme weather (e.g., extreme heat or freezing temperatures) and recommends appropriate actions.

### 5. Comprehensive Weather Agent
- **Task:**  
  Orchestrates all the individual agents to produce a full weather report, including current conditions, 5-day forecasts, sentiment analysis, and health alerts.
- **Key Function:**  
  Integrates data fetching, processing, sentiment evaluation, and email delivery into a single cohesive system.

---

## How It Works

1. **User Input:**  
   Users enter their location (city name or zip code) and email address via the Gradio interface.

2. **Data Retrieval:**  
   The Weather Fetcher Agent collects current weather and forecast data from the OpenWeatherMap API.

3. **Sentiment Analysis:**  
   The Sentiment Analyzer Agent uses Azure Text Analytics to interpret the emotional tone of the weather description, generating a sentiment response.

4. **Health & Safety Alerts:**  
   The Health & Safety Alerts Agent assesses temperature and humidity to provide safety advisories.

5. **Data Formatting:**  
   The Comprehensive Weather Agent consolidates the data into a structured HTML report.

6. **Email Delivery:**  
   The system sends the formatted weather report to the user's email address.

7. **Graphical Visualization:**  
   The system generates a line chart for the 5-day forecast temperature data and saves the image for later display in the email and the web interface.

---

## Setup Instructions

### Prerequisites

- Python 3.6 or later
- Required Python libraries (listed in `requirements.txt`)
- Azure subscription with access to Azure AI services
- OpenWeatherMap API key
- SMTP email configuration

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SmartWeather-agent-ai.git
   cd SmartWeather-agent-ai
