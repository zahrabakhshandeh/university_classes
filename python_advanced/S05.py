"""num1 = 3
if num1 % 2 == 0:
	print("even")
else:
	print("odd")"""
#for num in range(2,,2): # num = 0, 1, 2
#	print(num)

# range(2,10,3) 2,5,8
# def ===> 0
# stop ====> def ===> x
# step ===> def ===> 1
"""n = int(input("number of your numbers: "))
for i in range(n):
	num1 = int(input(f"your number_{i+1}: "))
	if num1 % 2 == 0:
		print("even")
	else:
		print("odd")
print("end")"""
"""num = int(input("your number: "))
for i in range(num): # 10
	if i % 6 == 0:
		print(i)"""
#num = int(input("your number: "))
"""for i in range(0, 20000, 6): # 2
	print(i)"""
"""sum_nums = 0
for i in range(4):
	num = int(input(f"number_{i+1}: "))
	#sum_nums = sum_nums + num
	sum_nums += num
print(sum_nums)"""
# f(3) ===> 3 * 2 * 1
"""num = 5000 # num =3
f = 1
for i in range(1, num + 1):
	f *= i
print(f)
f = str(f)
l = len(f)
print(l)"""

"""num = int(input("your number: "))
num2=0
for i in range (0,num,3):
	num2 += i
print(num2)"""
sum_even = 0
sum_odd = 0
str_max_even = "" # len = 0
str_max_odd = ""
#total_max = ""
for i in range(4):
	name = input(f"str_{i+1}: ")
	l = len(name)
	#if l > len(total_max):
	#	total_max = name
	if l % 2 == 0:
		sum_even += l
		if l > len(str_max_even):
			str_max_even = name
	else:
		sum_odd += l
		if l > len(str_max_odd):
			str_max_odd = name

avg = (sum_odd + sum_even) / 4
print(f"sum odd: {sum_odd}")
print(f"sum even: {sum_even}")
print(f"avg : {avg}")
print(f"max str even: {str_max_even}")
print(f"max str odd: {str_max_odd}")
total_max = str_max_odd
if len(total_max) < len(str_max_even):
	total_max = str_max_even
print(f"max str total: {total_max}")