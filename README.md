# Weather Application

This project is a simple web application built with Flask, a Python web framework, to retrieve and display weather information for a given city. It utilizes the OpenWeatherMap API to fetch current weather data.

## Features:
- Allows users to input a city name and retrieve the current weather information.
- Displays temperature, humidity, and weather conditions for the specified city.
- Uses Flask for handling HTTP requests and rendering HTML templates.
- Utilizes the requests library to make API calls to OpenWeatherMap.

## Usage:
1. Clone the repository to your local machine.
2. Set up a virtual environment if desired.
3. Obtain an API key from OpenWeatherMap and store it in a `.env` file as `OPENWEATHER_API_KEY=your_api_key`.
4. Run the Flask application by executing `python main.py` in your terminal.
5. Access the application in your web browser by navigating to `http://localhost:5000`.

## Libraries Used:
- Flask: A lightweight web framework for Python.
- requests: A library for making HTTP requests in Python.
- dotenv: A library for loading environment variables from a .env file.

**Note:** Ensure to keep your API key secure by not exposing it in any public repositories. Use environment variables or configuration files to store sensitive information securely.
