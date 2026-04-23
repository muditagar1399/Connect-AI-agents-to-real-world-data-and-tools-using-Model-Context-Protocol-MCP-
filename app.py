@app.get("/agent")
def agent(query: str):
    if "weather" in query.lower():
        city = query.split()[-1]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url).json()

     
        if "main" not in res:
            return {
                "error": "Could not fetch weather. Check city name or API key.",
                "api_response": res
            }

        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]

        return {"response": f"Weather in {city} is {temp}°C with {desc}"}

    return {"response": "Ask about weather like: weather jaipur"}
