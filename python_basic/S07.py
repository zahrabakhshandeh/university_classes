# Loop ===> for
# num = 3, num = 16, num= 3, num= 20
"""for i in range(4):
	num = int(input("your number: "))
	if num %2 == 0:
		print("even")
	else:
		print("odd")"""
# i = 0, i = 1, i = 2, ..., i = 4
"""for i in range(5):
	print(i)"""
"""num = int(input("number: "))
for i in range(num):
	if i % 2 == 0:
		print(i)"""
"""num = int(input("number: "))
# num = 5, i = 0, i = 2, i = 4
for i in range(0, num, 2):
	print(i)"""
# range(start, stop, step)
# start ====> 0
# step ====> 1
# 4! ==> 1 * 2 * 3 * 4
# i = 1, i = 2
num = int(input("your number: "))
f = 1
for i in range(1, num+1):
	f = f * i
print(f)
f = str(f)
print(f"\nlength of the result: {len(f)}")
# num = 4
# f = 1
# i = 1, f = 1 * 1 = 1
# i = 2, f = 1 * 2 = 2
# i = 3 , f = 2 * 3 = 6
# i = 4, f = 6 * 4 = 24