import numpy as np

'''
X 数据矩阵
'''


def kmeans(X, k, maxIt):
	numPoints, numDim = X.shape  # numPoints 数据点(也可以看成一行记录) numDim特征维度

	dataSet = np.zeros((numPoints, numDim + 1))  # 构造一个 numPoints行  numDim + 1 列的 数组  最后一列是存放每一次迭代的均值

	dataSet[:, :-1] = X  # 将X 赋值给 第一列到倒数第二列的数组 （最后一列没赋值 全部是0）

	#  随机初始化k个中心点
	#  : 所有列都要
	centroids = dataSet[np.random.randint(numPoints, size = k), :]
	centroids = dataSet[0:2, :]  # 指定中心点
	# 给最后一列标签列赋值 从1开始  range取前不取后
	# : 这里是每一行都要
	centroids[:, -1] = range(1, k + 1)

	#
	iterations = 0  # 循环多少次  从0开始
	oldCentroids = None

	# 迭代何时停止
	while not shouldStop(oldCentroids, centroids, iterations, maxIt):
		# 打印循环到第几轮的信息
		print("iterations = ", iterations)
		print("dataSet = ", dataSet)
		print("centroids = ", centroids)

		oldCentroids = np.copy(centroids)  # 不要使用等号赋值，两个object都还要用，我们想要得到更新其中一个 另外一个不变

		iterations += 1

		# 对每个中心点重新分类，更新(根据中心点和数据集重新分类)
		updateLabels(dataSet, centroids)

		# 归类之后算出新的中心点
		centroids = getCentroids(dataSet, k)

	return dataSet


# 停止的两种条件(1) 迭代次数大于设定的最大迭代次数 (2) 如果前后两次中心点的值 相等 说明数据已经收敛了 迭代结束
def shouldStop(oldCentroids, centroids, iterations, maxIt):
	if iterations > maxIt:
		return True
	return np.array_equal(oldCentroids, centroids)  # 比较值 不是对象


# 传入一个矩阵和一个中心点 centroids 形象的可以看做dataSet的一行  平面上的一些点
def updateLabels(dataSet, centroids):
	numPoints, numDim = dataSet.shape  # 使用shape函数 返回矩阵的行和列数

	for i in range(0, numPoints):  # 遍历每一行
		# 对第i行 最后一列赋值（归类）
		# 当前这个点 到 最近中心点的label返回赋值给 当前行的最后一列
		dataSet[i, -1] = getLabelFromClosestCentroids(dataSet[i, :-1], centroids)


# np.linalg.norm numpy内建的一个计算距离的函数

def getLabelFromClosestCentroids(dataSetRow, centroids):
	label = centroids[0, -1]  # 初始化label

	# 定义一个最小距离
	minDist = np.linalg.norm(dataSetRow - centroids[0, :-1])

	for i in range(1, centroids.shape[0]):  # 之前初始化从0开始 所以这里从1开始
		dist = np.linalg.norm(dataSetRow - centroids[i, :-1])
		if dist < minDist:
			minDist = dist
			label = centroids[i, -1]

	print("minDist:", minDist)
	return label


# 对于标签等于n矩阵找出来 对其求均值（也就是所有归为一类的点求均值）
def getCentroids(dataSet, k):
	result = np.zeros(k, dataSet.shape[1])
	for i in range(1, k + 1):
		oneCluster = dataSet[dataSet[:, -1] == i, :-1]
		result[i - 1, :-1] = np.mean(oneCluster, axis = 0)  # i - 1 是从0开始  axis = 0 对行求均值
		result[i - 1, -1] == i

	return result


if __name__ == '__main__':
	x1 = np.array([1, 1])
	x2 = np.array([2, 1])
	x3 = np.array([4, 3])
	x4 = np.array([5, 4])

	testX = np.vstack((x1, x2, x3, x4))  # 将四个点纵向的堆起来 组成一个矩阵

	result = kmeans(testX, 2, 10)

	print("final result:", result)
