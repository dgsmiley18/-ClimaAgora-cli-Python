import requests
import argparse
from bs4 import BeautifulSoup


def get_weather_info(location):
    # Accesses Google's website and retrieves the necessary information
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    html = requests.get(
        f"https://www.google.com/search?q=clima+agora+{location}", headers=headers
    ).content
    soup = BeautifulSoup(html, "html.parser")

    # Finds the necessary information
    city_name = soup.find("span", class_="BBwThe").text
    temp_min = soup.find("div", class_="gNCp2e").find("span").text
    temp_max = soup.find("div", class_="QrNVmd ZXCv8e").find("span").text
    temperature = soup.select_one("#wob_tm").text
    rain = soup.select_one("#wob_pp").text
    wind = soup.select_one("#wob_ws").text
    humidity = soup.select_one("#wob_hm").text
    today_info = soup.select_one("#wob_dc").text
    weather_condition = soup.select_one("#wob_dts").text.capitalize()
    try:
        alert_type = soup.select_one(".vk_h").text
        alert_time = soup.select_one("div.Uekwlc:nth-child(3)").text
    except:
        alert_type = "Alert: None"
        alert_time = ""

    return {
        "city_name": city_name,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "temperature": temperature,
        "rain": rain,
        "wind": wind,
        "humidity": humidity,
        "today_info": today_info,
        "weather_condition": weather_condition,
        "alert_type": alert_type,
        "alert_time": alert_time,
    }


if __name__ == "__main__":
    # Instantiates the ArgumentParser
    parser = argparse.ArgumentParser(
        prog="Weather", description="See today's weather directly from your terminal!"
    )

    # Adds the "--location" argument with an explanation
    parser.add_argument("-l", "--location", help="specify a location", default="+")
    args = parser.parse_args()

    # Displays the information on the console
    info = get_weather_info(args.location)
    print(f"🏙 City: {info['city_name']}")
    print(f"🌡️ Temperature: {info['temperature']}°C")
    print(f"\u2B06 Minimum: {info['temp_min']}° \u2B07 Maximum: {info['temp_max']}°")
    print("\u2614 Rain: " + info["rain"])
    print("🍃 Wind: " + info["wind"])
    print("Humidity: " + info["humidity"])
    print("Today's Condition: " + info["today_info"])
    print(info["weather_condition"])
    print("\033[33m{}\033[0m".format(info["alert_type"]))
    print("\033[33m{}\033[0m".format(info["alert_time"]))
