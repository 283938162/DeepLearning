##
#
# DEMO TEST
#
##


# 字典
d = {'a': 1, 'b': 2, 'c': 3}
print(d['c'])
exit()

# python 字典 dict {} 做统计
#
# list = ['a', 'b', 'c', 'a']
# d = {}
# for x in list:
# 	if x in d:
# 		d[x] += 1
# 	else:
# 		d[x] = 1
#
# 	print(d[x])

# list 中的applend
# list = []
# list.append((1,2))  # 向list中添加元组 Tuple ，这种数据结构很重要
# list.append("a")
# print(list)


# Tuple 索引也是使用[]

# t = (1,2,3)
# for x in range(len(t)):
# 	print(t[x])


# 使用场景[(),(),()]
# 使用sorted 对元组中第二个字段排序

# import operator
#
# dataSet = [([4.9, 3.0, 1.4, 0.2, 'Iris-A'], 0.5385164807134502),
# 		   ([4.7, 3.2, 1.3, 0.2, 'Iris-B'], 0.509901951359278),
# 		   ([4.6, 3.1, 1.5, 0.2, 'Iris-C'], 0.648074069840786)]
#
# dataSet.sort(key = operator.itemgetter(1), reverse = True)  # reverse参数boolean变量，默认为false（升序排列），定义为True时将按降序排列。
#
# print(dataSet)
#
# neighbors = []
#
# for x in range(2):
# 	neighbors.append(dataSet[x][0])
#
# print(neighbors)

# 读取CSV文件

# import csv
#
# filePath = r"F:\MLDSet\KNN\irisdata.txt"
#
# with open(filePath, 'r') as csvfile:
# 	lines = csv.reader(csvfile)
# 	print(lines)
# 	dataset = list(lines)
# 	# print(dataset)
#
# 	for x in range(len(dataset) - 1):
# 		# for y in range(4):
# 		# 	print(dataset[x][y], end = '	')
# 		# print()
# 		print(dataset[x])


# dataSet= ['RID', 'age', 'income', 'student', 'credit_rating', 'class_buys_computer']
#
#
# for x in range(len(dataSet)):
# 	print(dataSet[x])
#
#
# # 不要最后一个class 分类列
# for x in range(len(dataSet) - 1):
# 	print(dataSet[x])

#
# print(list[-1])  # class_buys_computer

# Python 数值类型

# # 随机函数
# import random
#
# # print(random.random)  # 返回一个对象属性
#
# r = random.random()
# print(r)  # Return the next random floating point number in the range [0.0, 1.0).
#
# print(float(r))


# print(list[0])
# rowDict = {}
#
# rowDict["name"] = 'zhangsn'
# rowDict["age"] = 12
# print(rowDict)

# for x in list:
#     print(x)

# for x in range(0,len(list)-1):
#     print(x)


# for x in range(4):
#     print(x)
