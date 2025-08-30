import requests
#requests库需要安装

def get_state(url):
    res = requests.get(url)
    print(res.status_code)

def read_topkeys(url):
    res = requests.get(url,params = {"city":"Shanghai"})
    data_dict = res.json()
    print(data_dict.keys())

# json 文件是dict+list多层交替着包，需要先取 dict，再取 list
def read_temp(url):
    res = requests.get(url)
    data_dict = res.json()
    print("温度C：")
    print(data_dict["current_condition"][0]["temp_C"])
    print("天气描述：")
    print(data_dict["current_condition"][0]["weatherDesc"][0]["value"])


def comp_weather(url):
    res = requests.get(url)
    data_dict = res.json()
    city = data_dict["nearest_area"][0]["region"][0]["value"]
    weather = data_dict["current_condition"][0]["weatherDesc"][0]["value"]
    temprature = data_dict["current_condition"][0]["temp_C"]
    print(f"城市：{city}，天气：{weather}，温度：{temprature}")


def main():
    url1 = "https://wttr.in/Beijing?format=j1"
    url2 = "https://wttr.in/Shanghai?format=j1"


    print("练习1：")
    get_state(url1)
    
    print("\n练习2：")
    read_topkeys(url2)

    print("\n练习3：")
    read_temp(url2)


    print("\n练习4：")
    comp_weather(url2)






if __name__ == "__main__":
    main()