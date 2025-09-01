import csv

def gen_csv(filename):
    with open(f"{filename}","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "age", "city"])

def read_file(filename):
    with open(f"{filename}","r") as file:
        for line in file:
            print(line.strip())

def add_data(filename,listname):
    # 如果不加 newline="" 写入新数据会隔一行
    with open(f"{filename}","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(listname)

def gen_csv_dict(filename,dictkey):
    with open(f"{filename}","w",newline="") as file:
        writer = csv.DictWriter(file,dictkey)
        writer.writeheader() #这一行会往文件里写入一行表头，如果已有表头，则无需这条，见add_data_dict

def add_data_dict(filename,dictkey,dictname):
    with open(f"{filename}","a",newline="") as file:
        writer = csv.DictWriter(file,dictkey)
        writer.writerow(dictname)

def main():
    print("练习1：写入一行数据到 CSV")
    gen_csv("test.csv")
    read_file("test.csv")
    print("test.csv文件已生成")

    print("\n练习2：追加 vs 覆盖")
    gen_csv("test2.csv")
    read_file("test2.csv")
    print("test2.csv文件已生成")
    add_data("test2.csv",["Alice",25,"shanghai"])
    add_data("test2.csv",["Bob",23,"Beijing"])
    read_file("test2.csv")

    print("\n练习3：通过字典写入 CSV")
    gen_csv_dict("test3.csv",["name", "age", "city"])
    read_file("test3.csv")
    print("test3.csv文件已生成")
    add_data_dict("test3.csv",["name", "age", "city"],{"name":"Alice","age":25,"city":"shanghai"})
    add_data_dict("test3.csv",["name", "age", "city"],{"age":23,"name":"Bob","city":"Beijing"})
    read_file("test3.csv")




if __name__ == "__main__":
    main()