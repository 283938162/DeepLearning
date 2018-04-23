from sklearn import svm

x = [[2, 0], [1, 1], [2, 3]]
y = [0, 0, 1]  # 归类标记  \  线下面是0 上面是1

clf = svm.SVC(kernel = 'linear')
clf.fit(x, y)

print("clf = ", clf)

# get support vectors
print("get support vectors = ", clf.support_vectors_)

# get indices of support vectors
print("get indices of support vectors = ", clf.support_)

# get number of support vectors for each class
print("get number of support vectors for each class = ", clf.n_support_)

# 测试数据
print(clf.predict([[2, 0]]))  # 预测结果与上面的数据一致
