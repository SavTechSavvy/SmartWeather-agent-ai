# SmartWeather AI Agent

## Abstract

**SmartWeather AI Agent** is a comprehensive, AI-powered weather reporting system that combines the capabilities of Azure AI agents and OpenAI models (GPT-4O-MINI) to deliver real-time weather data, sentiment analysis, and health and safety alerts. By integrating OpenWeatherMap for live weather information with Azure AI Services for natural language processing and sentiment analysis, this AI-powered solution provides personalized weather insights, actionable advisories, and detailed forecasts.

The goal of this application is to showcase the capabilities of an advanced AI agent, utilizing Azure AI and OpenAI technologies. This intelligent agent fetches real-time weather data, analyzes the sentiment of weather conditions, and generates health and safety alerts based on the forecasted environment. Through the integration of multiple AI models, SmartWeather AI not only enhances user interactions but also empowers data-driven decision-making and provides valuable insights in an interactive web interface and through email notifications. This solution highlights the transformative potential of AI in improving everyday life by making weather data more accessible and actionable.
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

## Gradio Interface
![image](https://github.com/user-attachments/assets/c78fcc50-cf7e-46d3-b173-4d1d03cc69e8)
## Email Output
![image](https://github.com/user-attachments/assets/14542726-b591-4f68-802b-cef646eba972)

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


---

## AI Agents in SmartWeather Agent AI

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

2. Install Required Dependencies: pip install -r requirements.txt
3. Run the Application:python weatherinsights.py
4. Access the Gradio Interface:
Once the server is running, the Gradio interface will be available at the provided URL (typically http://127.0.0.1:7860), where you can input the location and email to get the weather report and visualizations.

## Conclusion

In conclusion, the goal of this app is to showcase an AI agent that combines the capabilities of Azure AI, OpenAI, and weather forecasting to deliver insightful, actionable information to users. This project highlights the potential of AI agents in automating tasks, improving user experience, and making complex data more accessible and understandable. The integration of weather data, sentiment analysis, and health and safety alerts makes this app a practical tool for users seeking timely and relevant information based on weather conditions.
