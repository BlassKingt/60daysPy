import requests
import csv

def get_url(city):
    url = f"https://wttr.in/{city}?format=j1"
    return url

def get_data(city):
    url = get_url(city)
    temp_data = {}
    res = requests.get(url)
    full_json_dict = res.json()

    temp_data["city"] =  full_json_dict["nearest_area"][0]["region"][0]["value"]
    temp_data["temperature"] = full_json_dict["current_condition"][0]["temp_C"]
    temp_data["description"] = full_json_dict["current_condition"][0]["weatherDesc"][0]["value"]
    return temp_data

def save_csv(filename,fieldnames,cities):
    with open(f"{filename}","w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames)
        writer.writeheader()
        for city in cities:
            dict_data = get_data(city)
            writer.writerow(dict_data)


def read_file(filename):
    with open(f"{filename}","r") as file:
        for line in file:
            print(line.strip())

def main():
    cities = ["Beijing", "Shanghai", "Guangzhou"]
    filename = "weatherdata.csv"
    fieldnames= ["city","temperature", "description"]
    save_csv(filename,fieldnames,cities)

    read_file(filename)



if __name__ == "__main__":
    main()