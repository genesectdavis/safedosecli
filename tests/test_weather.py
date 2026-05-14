import sys
import os

sys.path.append(os.path.abspath("src"))

from weather import get_weather

def test_weather_api():
    temperature = get_weather()

    assert isinstance(temperature, (int, float))