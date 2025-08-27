# 练习1：文件遍历
# 写一段代码，把 app.log 的每一行都打印出来。
def readfile():
    with open("app.log","r") as file:
        for line in file:
            print(line.strip())

# 练习2：查找 ERROR
# 写一个判断语句，如果行里有 "ERROR"，就打印出来。
def is_error_in_line(line):
    # 要用lower避免大小写不同情况。注意：由于string不变性，必须在同一行写lower并判断，不能拆成2句。
    return ("error" in line.lower())
def find_error(line):
    if is_error_in_line(line):
        print(line)

# 练习3：存储结果
# 不是直接打印，而是先存到 errors 列表，最后统一输出。
def save_err_list(tline,tlist):
    tlist.append(tline)
    return tlist



def main():
    print("练习1：")
    readfile()

    print("\n练习2：")
    line1 = "2025-08-01 ERROR Database connection failed"
    line2 = "2025-08-01 ErrOr Database connection failed"
    line3 = "2025-08-01 Database connection Successful"
    find_error(line1)
    find_error(line2)
    find_error(line3)

    print("\n练习3：")
    err_list = []
    err_list = save_err_list(line1,err_list)
    err_list = save_err_list(line2,err_list)
    print(err_list)


if __name__ =="__main__":
    main()

