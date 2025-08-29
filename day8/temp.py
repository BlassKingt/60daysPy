
def get_score(D,name):
    score = D[f"{name}"]
    print(score)

def mod_score(D,name,score):
    D[f"{name}"] = score


def read_dic(D):
    for name,score in D.items():
        print(name,score)

def rm_score(D,name):
    del D[f"{name}"]



def main():
    print("练习1：访问字典")
    scores = {"Tom": 80, "Jerry": 92}
    get_score(scores,"Jerry")

    print("\n练习2：修改字典。\n在 scores 里添加 \"Anna\": 88，再修改 \"Tom\" 的成绩为 85。")
    mod_score(scores,"Anna", 88)
    print("Anna:")
    get_score(scores,"Anna")
    print("Tom:")
    get_score(scores,"Tom")
    mod_score(scores,"Tom", 85)
    print("Tom:")
    get_score(scores,"Tom")


#  练习4：遍历字典
#  打印每个学生的名字和成绩。
    print("\n练习4：遍历字典打印每个学生的名字和成绩。")
    read_dic(scores)


# 练习3：删除元素
# 删除 Jerry，再打印整个字典。
    print("\n练习3：删除元素。删除 Jerry，再打印整个字典。")
    rm_score(scores,"Jerry")
    read_dic(scores)




if __name__ == "__main__":
    main()