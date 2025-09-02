import requests

def get_url(city):
    city = city.lower()
    return f"https://wttr.in/{city}?format=j1"


def get_weather(city):
    url = get_url(city)
    res = requests.get(url)

    data_dict = res.json()

    city_name = data_dict["nearest_area"][0]["areaName"][0]["value"]
    weather = data_dict["current_condition"][0]["weatherDesc"][0]["value"]
    temp = data_dict["current_condition"][0]["temp_C"]

    res_data_dict = {"城市":city_name,"天气":weather,"温度":f"{temp} ℃"}
    return res_data_dict

    