#注：由于还未学习正则表达式等方法，本日的工具，将例如fox's这样的词视作与fox不同的词来统计

counts = {}

with open("test.txt","r") as file:
    for line in file:
        #根据空格分割
        split_line = line.split()
        #处理每个词
        for word in split_line:
            #lower化每个词
            t_word = word.lower()
            #清洗每个词可能含有的标点和空格
            t_word = t_word.strip(" !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~")
            #dict化统计每个词出现次数
            counts[t_word] = counts.get(t_word,0) + 1
Sort = sorted(counts.items(), key = lambda i:i[1], reverse=True)
for i in range(10):
    print("%s: %d"%(Sort[i][0],Sort[i][1] ))

#这里考虑多个第十名
#第十名的词对应的value
No10 = Sort[9][1]
#从Sort的第十一个键值对开始找
for item in Sort[10:]:
    if item[1] == No10:
        print("%s: %d"%(item[0],item[1] ))
    else:
        #如果第十一个的数量够不着第十的名次，则不需要再继续向后找了
        break


