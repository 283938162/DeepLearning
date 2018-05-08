class Employee:
	'所有员工的基类'
	empCount = 0
	def __init__(self, name = 'zhangsan'):
		print("init")
		print('name = ', name)

		

	# def __init__(self, name, salary):
	# 	self.name = name
	# 	self.salary = salary
	# 	Employee.empCount += 1

	def displayCount(self):
		print("Total Employee %d" % Employee.empCount)

	def displayEmployee(self):
		print("Name : ", self.name, ", Salary: ", self.salary)


# emp = Employee('zz',1010)
# emp.displayCount()
emp1 = Employee('lisi') # 这样实现多肽/重写的功能， 不传参数 init中默认参数生效,传的话覆盖
