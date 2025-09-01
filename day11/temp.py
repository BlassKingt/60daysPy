import json

# 要求：把它转成 JSON 字符串并打印出来（要求缩进 2 格，中文不要转义）
def Jstring(dictname):
    #res = json.dumps(dictname)
    res = json.dumps(dictname, indent= 2, ensure_ascii= False)
    #dumps的s是dump string 的意思，能够返回字符串
    print( res)

# 把 JSON 数据写到 weather.json 文件里
def save_json_file(dictname,filename):
    #json.dump不反回东西，可以直接写入文件，当然，文件要先打开
    with open(f"{filename}","w",encoding="utf-8") as file:
        json.dump(dictname,file,indent=2,ensure_ascii=False,sort_keys=True)

def check_file(filename):
    with open(f"{filename}","r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())

#从 weather.json 读取内容，并取出 "city" 和 "temp" 字段。
#另外还有一个json.loads，从str解析，必须输入string，其实就是把字符串转换为dict等
def read_jsonFile(filename):
    with open(f"{filename}","r",encoding="utf-8") as file:
        jsondata = json.load(file)
    return jsondata


def main():
    data = {"city": "上海", "temp": 26, "weather": "Cloudy"}
    print("1:")
    Jstring(data)

    print("\n2:")
    save_json_file(data,"weather.json")
    check_file("weather.json")

    print("\n3:")
    json_data = read_jsonFile("weather.json")
    print(f"city: {json_data['city']}")
    print(f"temp:{json_data['temp']}")




if __name__ == "__main__":
    main()
