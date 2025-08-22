# #功能1：文件操作
# 原始方法
# f = open("notes.txt","r")
# content = f.read()
# print(content)
# f.close

# #功能1 - 小练习1 用r模式读出并打印文件内容
# with open("notes.txt","r",encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# #功能1 - 小练习2 用w模式写入一句“hello world”然后再读出来，打印文件内容
# with open("notes.txt","w",encoding="utf-8") as file:
#     file.write("Hello World")
# with open("notes.txt","r",encoding="utf-8") as file:
#      content = file.read()
#      print(content)

# #功能1 - 小练习3 用a模式往文件末尾追加一行追加内容，然后再读出来，打印文件内容
# with open("notes.txt","a",encoding="utf-8") as file:
#     file.write("\n and more")
# with open("notes.txt","r",encoding="utf-8") as file:
#      content = file.read()
#      print(content)     

#############################################################
# #功能2：逐行读取
# #读取notes.txt，用for line in f逐行打印；打印时在前面加上“这一行是：”
# with open("notes.txt","r",encoding="utf-8") as f:
#     for line in f:
#         output = "这一行是：" + line
#         print(output)


############################################################
# #功能3：计数器
# #写一个列表item，用for循环统计它有几个元素，打印“总共有x个元素”
# count = 0
# items = ["a","b","c"]
# for i in items:
#     count += 1
# print("总共有 %d 个元素" % (count))

