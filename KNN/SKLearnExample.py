from sklearn import neighbors
from sklearn import datasets


#  调用sklearn中的knn算法

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()

# print("iris = ", iris)

# 好多分类器都有这样一个方法 fit 建立一个模型
knn.fit(iris.data, iris.target)

# 实例预测
predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])


print("target_names = ",iris.target_names)
print("predictedLabel = ",predictedLabel)  # 对应第一类花的名字 setosa

