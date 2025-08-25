# 函数练习：写一个 say_hi() 函数，返回字符串 "Hi!"
def say_hi():
    return "Hi!"

# 参数练习：写一个 multiply(a, b) 函数，返回 a*b。
def multiply(a,b):
    return a*b



# 返回值练习：写一个 is_even(n) 函数，判断一个数是不是偶数（返回 True/False）。
def is_even(n):
    if ( n % 2 == 0):
        return True
    else:
        return False 



# 条件判断练习：写一个 check_sign(n) 函数，如果大于 0 返回 "positive"，小于 0 返回 "negative"，否则返回 "zero"。
def check_sign(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"







def main():
    print("练习1：")
    str = say_hi()
    print(str)

    print("\n练习2：")
    x1, y1 = 4, 2
    print(f"{x1} x {y1} =")
    res = multiply(x1,y1)
    print(res)

    print("\n练习3：")
    x2, y2 = 4, 3
    print(f"{x2}是偶数吗？回答：{is_even(x2)}")
    print(f"{y2}是偶数吗？回答：{is_even(y2)}")

    print("\n练习4：")
    x3, y3, z3 = 4, -5, 0
    print(f"{x3}是{check_sign(x3)}")
    print(f"{y3}是{check_sign(y3)}")
    print(f"{z3}是{check_sign(z3)}")









if __name__ == "__main__":
    main()