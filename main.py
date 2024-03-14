from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")


@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city_name = request.form["city"]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(url)
        weather_data = response.json()
        if weather_data and "main" in weather_data and "temp" in weather_data["main"]:
            weather_data["main"]["temp"] -= 273.15
            weather_data["main"]["temp"] = int(weather_data["main"]["temp"])

    return render_template("index.html", weather_data=weather_data)


if __name__ == "__main__":
    app.run(debug=True)
