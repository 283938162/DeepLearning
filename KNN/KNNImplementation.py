import csv
import random
import math
import operator


# trainingSet 训练数据产生模型  形如,逗号隔开 5.1,3.5,1.4,0.2,Iris-setosa
# testSet 测试数据集


# 将原始数据一分为二，一部分作训练数据集产生模型 另一部分作为测试数据集
def loadDataset(filename, split, trainingSet = [], testSet = []):
	with open(filename, 'r') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)  # 将所有行转化成一个list的数据结构
		for x in range(len(dataset) - 1):
			for y in range(4):
				dataset[x][y] = float(dataset[x][y])  # //todo
			if random.random() < split:
				# if random.randrange(len(trainingSet)) < split:
				trainingSet.append(dataset[x])
			else:
				testSet.append(dataset[x])


# instace1,2 两个实例   length维度
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


# 从训练集每一个实例到测试集实例最近的 k 个值
def getNeighbors(trainingSet, testInstance, k):
	distances = []  # 定义一个存距离的容器
	length = len(testInstance) - 1  # 维度
	for x in range(len(trainingSet)):  # 训练集中的每一个实例到测试集的距离
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key = operator.itemgetter(1))  # 排序 取距离最近的k个邻居,默认升序排序即距离从小到大
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])  #
	return neighbors


# 根据每个邻居投票的个数排序,返回票数最多的分类值
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1), reverse = True)
	return sortedVotes[0][0]


# 对测试集中的每一个数据预测出一个分类，和实际真正的分类比较，多少是正确的，得出一个精确度
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		# print 'test'
		# test = testSet[x][-1]
		# print test
		# print 'pre'
		# pre = predictions[x]
		# print pre
		print('test: ' + repr(testSet[x][-1]))
		repr(testSet[x][-1])
		print('pre: ' + repr(predictions[x]))
		# if testSet[z][-1] == predictions[z]:
		#     correct += 1
		return (correct / float(len(testSet))) * 100.0


def main():
	# prepare data
	"""

	:rtype: object
	"""
	trainingSet = []
	testSet = []
	split = 0.70  # 阈值界定
	loadDataset(r'F:\MLDSet\KNN\irisdata.txt', split, trainingSet, testSet)
	# print('Train set: ' + repr(len(trainingSet)))
	# print('Test set: ' + repr(len(testSet)))

	print('TrainSet: ', trainingSet)
	print('TestSet: ', testSet)

	# generate predictions
	predictions = []
	k = 3  # knn 中的k 取最近的3个
	correct = []
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)  # 根据少数服从多数 result表示应该归类的值
		predictions.append(result)
		# print ('test: ' + repr(testSet))
		print('predictions: ' + repr(predictions))
		print('>predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))

		if result == testSet[x][-1]:
			correct.append(x)
		# print "len:"
		# print len(testSet)
		# print "correct:"
		# print len(correct)
	accuracy = (len(correct) / float(len(testSet))) * 100.0
	print('Accuracy: ' + repr(accuracy) + '%')


if __name__ == '__main__':
	main()
