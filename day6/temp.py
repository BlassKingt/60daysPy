import random
import string

# 练习1：随机整数
# 用 random.randint 生成 3 个 1–50 的随机数。
def rand_int(a,n):
    for _ in range(n):
        a.append( random.randint(1, 50) )


# 练习2：随机浮点数
# # 用 random.random 生成 2 个浮点数（保留 2 位小数）。
def rand_float(a,n):
    for _ in range(n):
        temp = random.random()
        temp = round(temp,2)
        # 注意：由于是float，若出现，例如，“0.50”自动省略后续，显示0.5
        # 可以直接格式化，但是后续如果要作为float用要记得float()
        temp_fm = f"{temp:.2f}"
        a.append(temp_fm)

# 练习3：随机选择
# 从列表 ["red", "blue", "green", "yellow"] 中随机选 5 次，看看结果。
def rand_Ch(a,n):
    Alters = ["red", "blue", "green", "yellow"] 
    for _ in range(n):
        a.append(random.choice(Alters))

# 练习4：随机字符串
# 用 random.choice 从 string.ascii_letters 里选 6 次，拼接成一个字符串。
def rand_str(n):
    strx = ""
    for _ in range(n):
        strx += random.choice(string.ascii_letters + string.digits)
    return strx
    #string.ascii_letters定义建议点开definition看下就明白了，就是英文字母字符串，并不是一个函数


arr1 = []
arr2 = [] 
arr3 = []


def main():
    print("练习1：随机整数")
    rand_int(arr1, 3)
    print("本次随机整数结果：")
    for i in range(3):
        print(arr1[i], end = " ")
    
    print("\n\n练习2：随机浮点数")
    rand_float(arr2,2)
    print("本次随机浮点数结果：",*arr2)
   
    print("\n练习3：随机选择")        
    rand_Ch(arr3,5)
    print("选择结果：")
    for i in range(5):
        print(arr3[i], end = " ")    

    print("\n\n练习4：随机选择字符串")   
    #注意，str不可变，因此如果已经通过str1=""初始化了string，则应该如下：+= 而不是 =    
    str1 = ""
    str1 += rand_str(6)
    print("随机字符串选择结果：")
    print(str1)    




if __name__ == "__main__":
    main()
