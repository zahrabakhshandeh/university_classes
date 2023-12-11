# function
#f(x, y)  = x * 4 + y
#f(2, 3) = 11
"""def f(x, y):
	res = x * 4 + y
	print(res)

def show_name():
	print("python")

x = int(input("number1: "))
y = int(input("number2: "))
f(x, y)
f(23, 5)
f(4, 5)
show_name()"""
def calu_avg(num1, num2): #num1=5,num2 = 6
	avg = (num1 + num2) / 2
	#print(avg)
	return avg

"""num1 = int(input("number1: ")) # 5
num2 = int(input("number1: ")) # 6
res1 = calu_avg(num1, num2) # calu_avg(5, 6)
print(f"avg of {num1} and {num2} = {res1}")
num1 = int(input("number1: ")) # 12
num2 = int(input("number1: ")) # 10
res2 = calu_avg(num1, num2)
print(f"avg of {num1} and {num2} = {res2}")
res3 = calu_avg(res1, res2)
print(f"avg of {res1} and {res2} = {res3}")"""
# +, -, *,/
def sum_(x, y):
	res = x + y
	return res

def minus(x, y):
	res = x - y
	return res

def div(x, y):
	if y != 0:
		res = x / y
		return res
	else:
		return "Error!"

def multi(x, y):
	res = x * y
	return res

while True:
	oper = input("+, -, *, /: ")
	num1 = int(input("number1: "))
	num2 = int(input("number2: "))
	if oper == "+":
		res = sum_(num1, num2)
	elif oper == "-":
		res = minus(num1, num2)
	elif oper == "*":
		res = multi(num1, num2)
	elif oper == "/":
		res = div(num1, num2)
	elif oper == "exit":
		break
	else:
		res = "not found"
	print(res)