# 写一个脚本，可以：
# 	1.	输入多个城市名（如 ["Beijing", "Shanghai", "Guangzhou"]）。
# 	2.	用 requests 请求 wttr.in 获取天气数据。
# 	3.	保存到 JSON 文件 weather.json，格式要清晰（缩进 2，中文显示正常）。

import requests
import json

def check_file(filename):
    with open(f"{filename}","r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())

def get_url(city):
    return f"https://wttr.in/{city}?format=j1"


def main():
    cities = ["Beijing", "Shanghai", "Guangzhou"]
    data_list = []
    for city in cities:
        url = get_url(f"{city}")
        res = requests.get(url)
        data_dict = res.json()

        city_name = data_dict["nearest_area"][0]["areaName"][0]["value"]
        weather = data_dict["current_condition"][0]["weatherDesc"][0]["value"]
        temp = data_dict["current_condition"][0]["temp_C"]
        
        data_dict_filtered = {"city": f"{city_name}", "weather": f"{weather}", "temp": f"{temp}℃"}

        data_list.append(data_dict_filtered)

    with open("Weather2.json","w",encoding="utf-8") as file:
        json.dump(data_list,file,indent=2,ensure_ascii=False)
    
    check_file("Weather2.json")

            
    


if __name__ == "__main__":
    main()