import subprocess
from weathernow import get_weather_info

def test_city_name():
    city_name = "SP"
    assert get_weather_info(city_name)["temperature"] is not None

def test_help():
    output = subprocess.check_output(["python", "weathernow.py", "--help"])
    assert b"specify a location" in output