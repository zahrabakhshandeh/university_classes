"""str1 = "Hi Python!"
print(str1[0])
# Slicing
print(str1[::2])
# methods
new_str = str1.lower()
print(new_str)
new_str = str1.upper()
print(new_str)"""
"""answer = input("yes or no: ").lower()
#answer = answer.lower()
if answer == "yes":
	print("Let's start")
elif answer == "no":
	print("u can't start")
else:
	print("not found")"""
# 20000
# p ==> 0
str1 = "python!Python,python,python"
c = str1.count("python")
#print(c)
"""i = str1.rindex("p")
i = str1.index("p")"""
#i = str1.rfind("a")
#i = str1.rfind("p")
#print(i)
num1 = int(input("number1: "))
num2 = int(input("nimber2: "))
sum_ = num1 + num2
# result: 10 + 15 = 25
# result: num1 + num2 = sum_
print("result:", num1, "+", num2, "=", sum_)
new_str = "result: {} + {} = {}".format(num1, num2, sum_)
print(new_str)
print(f"result: {num1} + {num2} = {sum_}")