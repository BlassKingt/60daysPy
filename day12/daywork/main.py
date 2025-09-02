import weather

def main():
    city = input("请输入城市名称（拼音）：")
    data_dict = weather.get_weather(city)
    # data_dict = {"城市":"shanghai","天气":"weather","温度":f"25℃"}
    for key,value in data_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()