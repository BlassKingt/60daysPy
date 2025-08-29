
def mod_score(D,name,score):
    D[f"{name}"] = score

def rm_score(D,name):
    del D[f"{name}"]

def read_dic(D):
    for name,score in D.items():
        print(name,score)

def get_avarage(D):
    ava = sum(D.values())/len(D)
    print(ava)

def get_max(D):
    # tmax = max(D)
    # 比较函数指针，应该要用dict.get，使比较value而不是字符串
    tmax = max(D, key=D.get)
    print(f"{tmax} {D[f'{tmax}']}")

def get_min(D):
    tmin = min(D, key = D.get)
    tmin_score = D[f"{tmin}"]
    print(f"{tmin} {tmin_score}")

def main():
    print("初始化成绩单：")
    scores = {"Bob": 88, "Charlie": 96, "longcharlie": 90 }
    read_dic(scores)

    print("\n")
    print("添加学生成绩：")
    mod_score(scores,"Alice",88)
    read_dic(scores)
    
    print("\n")
    print("修改学生成绩：")
    mod_score(scores,"Charlie",95)
    read_dic(scores)
    
    print("\n")
    print("删除学生成绩：")
    rm_score(scores,"Bob")
    read_dic(scores)

    # print(scores.values())
    # print(scores.keys())
    print("\n")
    print("学生成绩平均值：")
    get_avarage(scores)

    print("\n")
    print("最高学生成绩：")
    get_max(scores)

    print("\n")
    print("最低学生成绩：")
    get_min(scores)


if __name__ == "__main__":
    main()