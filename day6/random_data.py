import random
import string


def rand_int_list(n):
    a = []
    for _ in range(n):
        a.append( random.randint(1, 100) )
    return a


def rand_str(len):
    strx = ""
    for _ in range(len):
        strx += random.choice(string.ascii_letters + string.digits)
    return strx

def rand_str_list(n,len):
    listx = []
    for _ in range(n):
        listx.append(rand_str(len))
    return listx


def rand_usr_list(n):
    arr = []
    for _ in range(n):
        usr = {}
        usr["username"] = rand_str(6)
        usr["password"] = rand_str(8)
        usr["age"] = random.randint(18, 50)
        arr.append(usr)
    return arr


def main():
    # 生成 10 个随机整数（1–100）
    list1 = rand_int_list(10)
    print(f"10个随机整数的列表：{list1}")


    # 生成 5 个随机字符串（长度 6，只含字母和数字）
    list2 = rand_str_list(5,6)
    print(f"5个随机字符串的列表：{list2}")

    # 生成一个列表，里面包含 5 个用户，每个用户有：
    # username（随机 6 位字母数字）
    # password（随机 8 位字母数字）
    # age（随机整数，18–50）
    list3 = rand_usr_list(5)
    print(f"5个随机用户的列表：{list3}")



if __name__ == "__main__":
    main()
