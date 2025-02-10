import os
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

# Load environment variables from a .env file
load_dotenv()

project_connection_string = "eastus.api.azureml.ms;xxx-xxx-xx-xxx-xxxxx;aiagent;ai-basic-project-xxx"
openweathermap_api_key = "xxxxxxxxxxxxx0fb45a385"
email_password = "xxxxxxx"

# Create an Azure AI Client from a connection string
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(), conn_str=project_connection_string
)

# Create agents
with project_client:
    agent1 = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="data-processor",
        instructions="You are an agent that processes data.",
    )
    agent2 = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="weather-fetcher",
        instructions="You are an agent that fetches weather data.",
    )

# Azure Text Analytics API setup
def authenticate_azure_text_analytics():
    endpoint = "https://agent-ai-servicesxxxxx.openai.azure.com/"  # Your endpoint
    api_key = "xxxxxxxx" # Your API key

    # Authenticate and create the Text Analytics client
    credential = AzureKeyCredential(api_key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
    
    return text_analytics_client

# Sentiment Analysis with Azure Text Analytics
class SentimentAnalyzer:
    def __init__(self):
        self.client = authenticate_azure_text_analytics()

    def analyze_sentiment(self, text):
        try:
            # Call the sentiment analysis API
            response = self.client.analyze_sentiment(documents=[text])
            sentiment = response[0].sentiment

            sentiment_response = "Sentiment Analysis: "
            if sentiment == "positive":
                sentiment_response += "😊 The weather is great! You should feel happy and energetic."
            elif sentiment == "neutral":
                sentiment_response += "😐 It's an average day. You can stay calm and carry on."
            else:
                sentiment_response += "😟 It might be a gloomy day. Try to relax indoors and take it easy."

            return sentiment_response
        
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            return "Sorry, there was an error processing the sentiment."

# Weather Fetcher Class
class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, location):
        if location.isdigit():
            url = f"http://api.openweathermap.org/data/2.5/weather?zip={location},us&appid={self.api_key}&units=metric"
        else:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch weather data"}

# Weather Forecast Fetcher Class
class WeatherForecastFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_forecast(self, location):
        if location.isdigit():
            url = f"http://api.openweathermap.org/data/2.5/forecast?zip={location},us&appid={self.api_key}&units=metric"
        else:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            forecast_list = data['list'][:5]  # Get the forecast for the next 5 time points
            return forecast_list
        else:
            return None

# Email Sending Class
class EmailSender:
    def send_email(self, subject, body, to_email):
        from_email = "joe.doe@gmail.com"
        password = email_password

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))  # Changed to 'html' for rich formatting

        # Send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

# Health and Safety Alerts based on weather
class HealthAndSafetyAlerts:
    def get_health_advisories(self, temperature, humidity):
        # Generate health alerts based on weather conditions
        if temperature > 35:
            return "⚠️ Extreme heat alert! Stay hydrated and avoid outdoor activities."
        elif temperature < 0:
            return "⚠️ Freezing temperatures! Dress warmly and limit outdoor exposure."
        elif humidity > 80:
            return "⚠️ High humidity! Stay cool and avoid prolonged exposure to the heat."
        return "No health advisories for this weather."

# Comprehensive Weather Agent
class ComprehensiveWeatherAgent:
    def __init__(self, project_client, weather_fetcher, forecast_fetcher, email_sender, sentiment_analyzer, health_and_safety_alerts):
        self.weather_fetcher = weather_fetcher
        self.forecast_fetcher = forecast_fetcher
        self.email_sender = email_sender
        self.sentiment_analyzer = sentiment_analyzer
        self.health_and_safety_alerts = health_and_safety_alerts

    def process_all(self, location, to_email):
        # Fetch current weather
        weather_data = self.weather_fetcher.get_weather(location)
        current_weather = f"The current temperature in {location} is {weather_data['main']['temp']}°C with {weather_data['weather'][0]['description']}."

        # Fetch weather forecast
        forecast = self.forecast_fetcher.get_forecast(location)

        # Get sentiment analysis for the current weather description
        sentiment_response = self.sentiment_analyzer.analyze_sentiment(weather_data['weather'][0]['description'])

        # Get health advisories
        health_advisory = self.health_and_safety_alerts.get_health_advisories(weather_data['main']['temp'], weather_data['main']['humidity'])

        # Prepare detailed email content
        details = f"""
        <html>
        <body>
        <h2>Weather Update for {location}:</h2>
        <hr>
        <h3>🌡️  <strong>Current Weather:</strong></h3>
        <ul>
            <li>Temperature: {weather_data['main']['temp']}°C</li>
            <li>Condition: {weather_data['weather'][0]['description']}</li>
            <li>Humidity: {weather_data['main']['humidity']}%</li>
            <li>Wind Speed: {weather_data['wind']['speed']} m/s</li>
        </ul>

        <h3>🌦️  <strong>5-Day Forecast:</strong></h3>
        <ul>
            {self.format_forecast(forecast)}
        </ul>

        <h3>📝 Sentiment Analysis:</h3>
        <p>{sentiment_response}</p>

        <h3>⚠️ Health & Safety Alerts:</h3>
        <p>{health_advisory}</p>

        <hr>
        <p>Stay safe and informed!</p>
        </body>
        </html>
        """
        
        # Send detailed email
        self.email_sender.send_email("Detailed Weather Information", details, to_email)
        return details

    def format_forecast(self, forecast):
        formatted_forecast = ""
        for day in forecast:
            dt_txt = day['dt_txt']
            temp = day['main']['temp']
            description = day['weather'][0]['description']
            formatted_forecast += f"<li>{dt_txt}: {temp}°C, {description}</li>"
        return formatted_forecast

    def generate_forecast_graph(self, forecast):
        dates = [f['dt_txt'] for f in forecast]
        temps = [f['main']['temp'] for f in forecast]

        plt.figure(figsize=(10, 5))
        plt.plot(dates, temps, marker='o', linestyle='-', color='b')
        plt.title('5-Day Temperature Forecast')
        plt.xlabel('Date and Time')
        plt.ylabel('Temperature (°C)')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('forecast_graph.png')
        return 'forecast_graph.png'

# Gradio Interface with Forecast Visualization
def weather_interface(location, email):
    weather_fetcher = WeatherFetcher(api_key=openweathermap_api_key)
    forecast_fetcher = WeatherForecastFetcher(api_key=openweathermap_api_key)
    email_sender = EmailSender()
    sentiment_analyzer = SentimentAnalyzer()
    health_and_safety_alerts = HealthAndSafetyAlerts()
    comprehensive_agent = ComprehensiveWeatherAgent(project_client, weather_fetcher, forecast_fetcher, email_sender, sentiment_analyzer, health_and_safety_alerts)
    
    # Get weather and forecast
    details = comprehensive_agent.process_all(location, email)
    forecast = comprehensive_agent.forecast_fetcher.get_forecast(location)
    forecast_image = comprehensive_agent.generate_forecast_graph(forecast)

    # Return both text and image
    return details, forecast_image

# Create Gradio Interface
gr_interface = gr.Interface(
    fn=weather_interface,
    inputs=[gr.Textbox(label="Location"), gr.Textbox(label="Email")],
    outputs=["html", "image"],
    title="Comprehensive Weather Agent",
    description="Enter your location and email to get weather details, sentiment insights, health & safety alerts, and a 5-day forecast graph.",
)

gr_interface.launch()
