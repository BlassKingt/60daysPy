#今日综合小工具：文件行数读取器
#打印notes.txt的每一行
#打印总行数

count = 0
with open("notes.txt","r") as file:
    for line in file:
        count += 1
        print("第%d行是:%s"%(count,line))
        
print("该文件总共有%d行"%count)