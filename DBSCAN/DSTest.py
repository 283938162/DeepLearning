import numpy as np

# l = [(1, 2), (3, 4)]
# ll = [[1, 2], [3, 4]]
# lll = np.array(ll)
#
# print("l = ",l)
# print("ll = ",ll)
# print("lll = ",lll)

# online = [(22, 1558), (12, 40261), (22, 1721)]
# print(online)
#
# x = np.array(online)
# print(x)
#
# y = x.reshape(-1, 2)
# print(y)
#
# z = y[:, 0:1]
# # z = y[:, 1]
# print(z)
#
# c = np.array([[1, 2, 3], [4, 5, 6]])
# print(c)
# d = np.array([(22, 1558), (12, 40261), (22, 1721)])
# print(d)

# reshape  要记住，python默认是按行取元素

# print(d.reshape(2, 3))

# # 获取一列
# x1 = d[:,0]  # 获取第一列数据 默认按行展示  [22 12 22]
#
# # 将 获取第一列的内容按列展示
# y1 = d[:,0].reshape(-1,1)  #  等价于 y2 = d[:,0:1]
# y2 = d[:,0:1]
#
# x = d[:]
#
#
# print(x)

#
# labels = [1, 2, 3, 4,]
#
# if labels[labels[:] == 2]:
# 	print("Hello!")
# elif labels[labels[:] == 5]:
# 	print("Hi!")
# else:
# 	print("Sorry")
#
# print(len(labels))
#
# x = np.array(labels)
# print(x)



# 使用set对list集合进行去重
lables =  [1, 2, 3, 4,5,1,3]

print(set(lables))
