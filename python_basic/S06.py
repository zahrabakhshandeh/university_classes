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
"""num1 = int(input("number1: "))
num2 = int(input("nimber2: "))
sum_ = num1 + num2
# result: 10 + 15 = 25
# result: num1 + num2 = sum_
print("result:", num1, "+", num2, "=", sum_)
new_str = "result: {} + {} = {}".format(num1, num2, sum_)
print(new_str)
print(f"result: {num1} + {num2} = {sum_}")"""
# join, split
"""str1 = "I am learning Python!"
words = str1.split(" ")
print(words)"""
"""list1 = ["Python", "Java", "C++"]
new_str = " ".join(list1)
print(new_str)"""
"""str1 = "hi python! python"
new_str = str1.replace("python", "java")
print(new_str)"""
# Search ====> in, not in
str1 = input("first Str: ") # hi python
sub_str = input("sub str: ") # python
if sub_str in str1: # True
	sub_str2 = input("sub str2: ") # java
	new_str = str1.replace(sub_str, sub_str2)
	# hi java
else:
	new_str = str1 + sub_str
print(new_str)