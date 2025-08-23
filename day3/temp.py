#小练习1：打印当前目录下的所有文件名。

import os
def prac1():
    files = os.listdir(".")
    print("当前目录下的所有文件名：")
    for file in files:
        print(file)


#小练习2：写一个循环，打印出目录下所有以 .txt 结尾的文件。
def prac2():
    print("当前目录下所有以 .txt 结尾的文件：")
    files = os.listdir(".")
    for file in files:
        if file.endswith(".txt"):
            print(file)
        else:
            continue

#小练习3：创建一个 test1.txt，把它重命名为 test_renamed.txt。
def prac3():
    print("创建：test1.txt")
    with open("test1.txt","w") as f:
        f.write("This file's name is test1.txt")
    #看一下现在有哪些文件
    prac2()
    #rename
    print("现在重命名")
    src = "test1.txt"
    dst = "test_renamed.txt"
    #如果已存在，先删除
    if os.path.exists(dst):
        print("%s已存在，先删除"%dst)
        os.remove(dst)
    os.rename(src,dst)
    prac2()


#小练习4：用 enumerate 给一个列表自动编号并打印结果。
def prac4():
    print("给文件列表自动编号")
    files = os.listdir(".")
    for Num,filename in enumerate(files,start=1):
        print(f"{Num}.{filename}")


#主函数
def main():
    print("\n小练习1:")
    prac1()

    print("\n小练习2:")
    prac2()

    print("\n小练习3:")
    prac3()

    print("\n小练习4:")
    prac4()


if __name__ == "__main__":
    main()
