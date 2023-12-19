from random import *
# ====> x
#  ====> y
# y > x
# y < x
# y = x

x = randint(1, 100)
print(x)
c_g = 0
c_s = 0
y = randint(5, 10) # 8
print(y)
for i in range(y): # i = 0, i = 1, ..
	user = int(input("number: "))
	chan = y - (i+1)
	if user > x:
		c_g += 1
		print(f"your number > my number ({chan})")
	elif user < x:
		c_s += 1
		print("your number < my number ({chan})")
	else:
		print("are equal!")
		break
print(c_g)
print(c_s)