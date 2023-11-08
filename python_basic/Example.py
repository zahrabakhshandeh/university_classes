num1 = float(input("Enter a number ? "))
num2 = float(input("Enter another number ? "))
num3 = float(input("number : "))
num4 = float(input("number : "))
# 120, 200, 300, 1800
max_num = num1
if num2 > max_num:
	max_num = num2
if num3 > max_num:
	max_num = num3
if num4 > max_num:
	max_num = num4
print(max_num)