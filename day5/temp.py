#基于py的正则式小练习
import re

#练习1：固定匹配
def exact_match(str):
    pattern = r"cat"
    print(re.match(pattern,str))


#练习2：数字匹配
def num_match(str):
    pattern = r"\d+"
    print(re.match(pattern,str))


#练习3：尝试用 re.match(r"^\w+@\w+\.\w+$", email) 判断 "abc@test.com" 是否合法
def email_match(str):
    pattern = r"^\w+@\w+\.\w+$"
    if re.match(pattern,str):
        print(f"邮箱:{str}合法")
    else:
        print(f"邮箱:{str}非法")


def main():
    print("练习1：")
    str1 = "cat123"
    str2 = "dogcat"
    exact_match(str1)
    exact_match(str2)

    print("\n练习2：")
    str3 = "123"
    str4 = "abc"
    str5 = "45a"
    num_match(str3)
    num_match(str4)
    num_match(str5)

    #print(re.match(r"\bcat\b","cat-dog"))

    print("\n练习3：")
    #可以发现小练习只是简单匹配，在工具中可以进一步要求
    email1 = "abc@test.com"
    email2 = "_@adas._net" 
    email3 = "example@sub.domain.co.uk"
    email_match(email1)
    email_match(email2)
    email_match(email3)




if __name__ == "__main__":
    main()