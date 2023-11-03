# conditions
# if, else
"""num1 = 100
num2 = 50
if num1 >= num2:
	print(num1)
if num2 > num1:
	print(num2)
if num1 >= num2:
	print(num1)
else:
	print(num2)"""
"""num1 = int(input("Enter your number: "))
if num1 % 2 == 0:
	print("even")
else:
	print("P")"""
"""num1 = int(input("your number: "))
if num1 < 0:
	num1 = -num1
print(num1)"""
#score = float(input("Enter number: "))
# score >= 10 ===> 7
# score < 10 ===> 5
"""if score >= 10:
	print("yes")
	score = 0.07 * score + score
else:
	print("no")
	score = 0.05 * score + score
print("new score: ", score)"""

"""num1 = int(input("Enter your hoogoogh ")) 
if num1 >= 5000:
	num1 = num1 - 0.06 * num1
else:
	num1 = num1 - 0.04 * num1
print(num1)"""
"""cmd = input("yes or no: ")
if cmd == "yes":
	print("yes")
else:
	print("you can not")"""

# if book == "python":
#     ..........
# else if book == "c++":
#     ...........
# else if book == "java":
#      ..........
# else if book == "c":
#       ..........
# else:
#      ...........
score = float(input("your score:"))
if score > 20 or score < 0: # 23
	print("out of range![0-20]")
elif score >= 17: # 19
	print("A++")
elif score >= 14:
	print("A+")
elif score >= 10:
	print("A")
else:
	print("B")

