from sklearn.feature_extraction import DictVectorizer  # DictVectorizer 规范化sklearn数据输入的要求 Integer
import csv  # csv python自带的包 不需要额外安装 3.2之前之后 api有变动
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

# Read in the csv file and put features into list of dict and list of class label
allElectronicsData = open(r'F:\MLDSet\DecisionTree\AllElectronics.csv', 'rt')
reader = csv.reader(allElectronicsData)  # read cvs file by line
headers = next(reader)  # 打印头行 ['RID', 'age', 'income', 'student', 'credit_rating', 'class_buys_computer']

print("headers:\n", headers)

featureList = []
labelList = []  # class value

for row in reader:
    labelList.append(row[len(row) - 1])  # 读取每一行的最后一个label值
    rowDict = {}
    for i in range(1, len(row) - 1):
        # print("row[i] = ", row[i])
        rowDict[headers[i]] = row[i]  # {'age': 'youth', 'student': 'no', 'income': 'high', 'credit_rating': 'fair'}#
        # print("rowDict = ", rowDict)
    featureList.append(rowDict)

print("featureList: \n" + str(featureList))
print("labelList: \n" + str(labelList))

# Vetorize features
vec = DictVectorizer()

dummyX = vec.fit_transform(featureList).toarray()

print("dummyX: \n" + str(dummyX))
print("feature_names:\n", vec.get_feature_names())

# vectorize class labels
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY: \n", str(dummyY))

# 上面的操作只是对数据的预处理

# Using decision tree for classification
# clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='entropy')  # 参数声明使用信息熵的 默认是id3 curd
clf = clf.fit(dummyX, dummyY)  # 构建决策树
print("clf: \n" + str(clf))

#
# Visualize model  创建dot文件 写出决策树信息
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

# 使用构建号的决策树 预测
oneRowX = dummyX[0, :].reshape(1, -1)
print("oneRowX: " + str(oneRowX))

# 测试模型
newRowX = oneRowX
newRowX[0][0] = 1
newRowX[0][2] = 0

print("newRowX: " + str(newRowX))

predictedY = clf.predict(oneRowX)
print("predictedY: " + str(predictedY))
