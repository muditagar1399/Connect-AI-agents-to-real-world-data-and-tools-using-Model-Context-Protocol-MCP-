from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "b1b87699e0ec89e0efbc2f34092bb1d1"

@app.get("/")
def home():
    return {"message": "AI MCP Agent Running"}

@app.get("/agent")
def agent(query: str):
    if "weather" in query.lower():
        city = query.split()[-1]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url).json()

        if "main" not in res:
            return {
                "error": "Could not fetch weather",
                "api_response": res
            }

        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]

        return {"response": f"Weather in {city} is {temp}°C with {desc}"}

    return {"response": "Ask about weather like: weather jaipur"}
