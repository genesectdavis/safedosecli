import requests

def get_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-23.55&longitude=-46.63&current_weather=true"
    )

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise Exception("Erro ao consultar API")

    data = response.json()

    return data["current_weather"]["temperature"]