import requests

def get_url():
    city_raw = input("请输入城市（拼音）：")
    city = city_raw[0].upper() + city_raw[1:]
    url = f"https://wttr.in/{city}?format=j1"
    return url

def get_data(url):
    res = requests.get(url)
    data_dict = res.json()
    city = data_dict["nearest_area"][0]["region"][0]["value"]
    weather = data_dict["current_condition"][0]["weatherDesc"][0]["value"]
    temprature = data_dict["current_condition"][0]["temp_C"]
    return city, weather, temprature

def show_weather( city, weather, temprature ):
    print(f"城市: {city}\n天气: {weather}\n温度: {temprature}℃")


def main():
    url = get_url()
    
    city, weather, temprature = get_data(url)

    show_weather( city, weather, temprature )



if __name__ == "__main__":
    main()