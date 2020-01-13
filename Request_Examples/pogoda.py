"""
Napisz program wyswietlajacy pogode dla wskazanej przez
uzytkownika lokalizacji.
Aplikacja ma działąć w trybie tekstowym:
Przykład użycia:
python pogoda.py warsaw
1. Skorzystaj z sys.argv
2. Obsłuż sytuację, gdy ktoś nie poada lokalizacji
3. Użyj namedtuple
4. Utwórz czytelne funkcje - get_location_id, get_location_weather, report_weather
5. Zabezpiecz się przed wykonaniem kodu w momencie importu
"""
import sys

from collections import namedtuple
import requests

Weather = namedtuple('Weather', ['location_name', 'the_temp', 'air_pressure', 'humidity'])


def get_loaction_id(location_name):
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={location_name}")
    return resp.json()[0]['woeid']


def get_location_weather(location_id):
    resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/")
    location = resp.json()['title']
    curr_data = resp.json()["consolidated_weather"][0]
    weather = Weather(
        location_name=location,
        the_temp=curr_data['the_temp'],
        air_pressure=curr_data['air_pressure'],
        humidity=curr_data['humidity']
    )
    return weather


def weather_report(weather):
    report = f"""Pogoda w {weather.location_name}
temperatura: {weather.the_temp}
wilgotnosc: {weather.humidity}
cisnienie: {weather.air_pressure}
"""
    return report

if __name__ == "__main__":
    try:
        location_name = sys.argv[1]
        location_id = get_loaction_id(location_name)
        weather = get_location_weather(location_id)
        report = weather_report(weather)
        print(report)
    except IndexError:
        print("Podaj nazwe lokalizacji")