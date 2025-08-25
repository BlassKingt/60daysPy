# 写一个小型计算器，能完成：
# 加法、减法、乘法、除法

# 用户输入两个数和一个运算符，程序输出结果。

def calc(a, b, op):
    if (op == "+"):
        return a+b
    elif (op == "-"):
        return a-b
    elif (op == "*"):
        return a*b
    elif (op == "/"):
        if b == 0:
            return "除数为0，无法计算"
        else:
            return a/b
    else:
        return "非法运算符"





def main():
    #input给的都是字符串
    x = float(input("请输入第一个数: "))
    #注意排除输入空格干扰
    oper = input("请输入运算符 (+ - * /):").strip()
    y = float(input("请输入第二个数:"))
    res = calc(x, y, oper)
    print(f"结果是：{res}")



if __name__ == "__main__":
    main()