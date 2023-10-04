# conditions
# if ===> body
# if True ====> body run
# if False ===> body dosn't run
"""num1 = 20
num2 = 30
if num2 < num1:
	num2 = num2 + 2
	print(num1)
print(num2)"""
# if
# else
"""num1 = 21
if num1 % 2 == 0: # False
	print("even") 
else: 
	print("odd") """
"""num1 = -20
if num1 >= 0:
	print(num1)
else:
	num1 = -1 * num1
	print(num1)"""
"""num1 = -30
if num1 < 0: # T
	num1 = -1 * num1 # 30
print(num1) # 30"""
"""score = 4
if score < 10:
	print("didn't pass")
else:
	print("passed")"""
#score = float(input("enter your score: "))
#score = float(score)
#print(score + 2)
#name = input("student name: ")
#age = int(input("student age: "))
#score = float(input("student score: "))
#print(name, age, score)
"""if score < 10:
	print("didn't pass")
else:
	print("passed")"""
# ..........Example...........
# limit : score <= 20 and score >= 0
# score >= 18 ===> A++
# score < 18 and score >= 15 ==> A+
# score < 15 and score >= 10 ==> A
# score < 10 ===> B
"""score = float(input("student score: "))
if score > 20 or score < 0:
	print("out of range!")
elif score >= 18:
	print("A++")
elif score >= 15:
	print("A+")
elif score >= 10:
	print("A")
else:
	print("B")"""

#500>=10%
#200>=200and<500 5%
price = int(input("Enter your number: "))
if price < 0 :
	price = "out of rage"
elif price >= 500:
	price = 0.9 * price
elif price >= 200 :
	price = 0.95 *price
print(price)