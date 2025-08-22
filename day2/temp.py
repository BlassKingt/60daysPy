#小练习

# #split
text = "I love Python so much"
# #练习1：按空格切割，打印结果
# output = text.split("o")
# print(output)
# #练习2：按字母‘o’切割，打印结果
output = text.split("o")
print(output)

######################################
# #lower/strip
# word = " Hello, "
# #练习1：转小写
# output = word.lower()
# print(output)
# #练习2：去掉逗号和空格。注意strip的参数chars是指全部要搜索去除的字符，而不是指按字符串去除
# output2 = word.strip(" ,")
# print(output2)
# #个人强化练习：什么是strip认为的“中间”
# word2 = "aabbccMIDDLEccddaa"
# clean_word2 = word2.strip("abcd")
# print(clean_word2)

######################################
# #字典dict计数
# #注意words是一个[set]
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# #练习：用字典统计每个水果出现的次数
# counts = {}
# for fruit in words:
#     counts[fruit] = counts.get( fruit, 0 ) +  1
# print(counts)
# # for fruit, count in counts.items():
# #     print(f"'{fruit}': {count}")
# #     print("%s : %d" %(fruit, count))

######################################
# #排序
# counts = {"apple":3,"orange":1,"banana":2}
# # #练习：按出现次数从大到小排序，打印结果
# # #注：1.counts和counts.items()的区别：
# # #    如果不写.items()，则是对counts的key排序————
# # #    返回的是作为key的fruits，而不是key-value的键值对
# # #   2.lambda函数中的i可以叫任何名字，但是:前后两个名字要一致，指的是对输入的参数所做的操作，
# # #    在sorted中也就是前面的迭代对象。
# output = sorted(counts.items(), key = lambda i:i[1], reverse = True)
# print(output)

# #注意：
# # 1.sorted的key需要给到函数，它是对函数的引用而不是调用，所以不需要输入参数
# # 2.iterable（sorted的第一个参数）和key，要保证二者操作的目标对象是一致的
# # 例如，若只需要返回key，可以这样实现：
# output = sorted(counts, key = counts.get, reverse = True)
# print(output)

# #可以看到get函数需要key，而前面的counts提供了key。
# # （而不是counts.items()，那样提供的key-value不可作为get的参数）
