import os
from flask import Flask, render_template, request
import requests
import urllib.parse

app = Flask(__name__)

# ================= CONFIG =================
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
PLACES_API_KEY = os.getenv("PLACES_API_KEY", "")
# ==========================================

def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(city)}&appid={WEATHER_API_KEY}&units=metric"
        data = requests.get(url).json()
        if data.get("cod") != 200:
            return f"Error: {data.get('message', 'Unknown')}"
        return f"{data['main']['temp']} °C"
    except Exception as e:
        return f"Error fetching weather: {e}"

def get_famous_places(city):
    try:
        query = urllib.parse.quote(f"famous places in {city}")
        url = f"https://serpapi.com/search.json?engine=google_local&q={query}&api_key={PLACES_API_KEY}"
        data = requests.get(url).json()
        places = [p.get("title") for p in data.get("local_results", [])]
        return places or ["No famous places found"]
    except Exception as e:
        return [f"Error fetching places: {e}"]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            return render_template("index.html", error="City name cannot be empty.")
        temperature = get_weather(city)
        places = get_famous_places(city)
        return render_template("city_info.html", city=city, temperature=temperature, places=places)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
