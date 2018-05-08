from numpy import genfromtxt  # 将csv数据转化成numpy
import numpy as np
from sklearn import linear_model

datapath = r"Delivery_Dummy.csv"
data = genfromtxt(datapath, delimiter = ",", skip_header = 1)  # 转换成 numpy array的形式

# print(data)


x = data[:, :-1]
x1= np.delete(x,2,axis =1)
y = data[:, -1:]
# y = data[:, -1]

print(x)
print(x1)
# print(y)

def fit_predict(x,y):
	mlr = linear_model.LinearRegression()

	mlr.fit(x, y)

	print(mlr)
	print("coef:", mlr.coef_)

	print("intercept:", mlr.intercept_)

	# xPredict = [90, 2]
	xPredict = np.array([90, 2, 0, 1]).reshape(1, -1)
	print('xPredict:', xPredict)
	yPredict = mlr.predict(xPredict)

	print("predict:", yPredict)

fit_predict(x,y)