# 今日最终练习

# email_checker.py：
# 请输入邮箱: test@example.com
# 结果: 合法邮箱 
# 请输入邮箱: abc@com
# 结果: 非法邮箱

#额外再加要求，要求邮箱:
# 1.开头(@前)是字母或数字
# 2.结尾（最后一个.后）可以支持@domain.co.uk但不支持@domain._net
# 3.不可以出现连续的--符号

import re

def email_check(email):
    pattern = r"^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(pattern,email):
        print("结果：非法邮箱")
        return
    
    noconti_pattern = r"-{2,}"
    local_part = email.split('@')[0]
    if re.search(noconti_pattern, local_part):
        print("结果：非法邮箱")
        return
    else: 
        print("结果：合法邮箱")
        return



def main():
    email = input("请输入邮箱：")
    email_check(email)


if __name__ == "__main__":
    main()