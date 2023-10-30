# +, *, -
sum_nums = lambda num1, num2 : num1 + num2
multi_nums = lambda num1, num2 : num1 * num2
minus_nums = lambda num1, num2 : num1 - num2
f1 = lambda x: x + 5
opr = input("+ or - or *: ")
num1 = int(input("num1: "))
num2 = int(input("num2: "))
if opr == "+":
	res = sum_nums(num1, num2)
	print(res)
elif opr == "-":
	res = minus_nums(num1, num2)
	print(res)
else:
	res = multi_nums(num1, num2)
	print(res)
