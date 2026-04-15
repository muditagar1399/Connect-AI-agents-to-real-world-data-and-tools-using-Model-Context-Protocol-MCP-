from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "014371a4d6855c5e37e20ed44eed8504"

@app.get("/")
def home():
    return {"message": "AI MCP Agent Running"}

@app.get("/agent")
def agent(query: str):
    if "weather" in query.lower():
        city = query.split()[-1]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url).json()

        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]

        return {"response": f"Weather in {city} is {temp}°C with {desc}"}

    return {"response": "Ask about weather like: weather jaipur"}
