### String
# "", ''
var1 = "Python"
# index 012345
#          -2-1
# print(var1[10]) # IndexError
#print(var1[-1])
# even ===> 2, 3
var2 = "c++"
# index 012
# odd ===> 1
# length ===> len()
#l_var2 = len(var2)
#print(l_var2)
#middle = l_var2 // 2
#middle = l_var2 / 2
#middle = int(middle)
#print(var2[middle])
"""var2 = "python" # len ===> 6 ===> 2, 3
l_var = len(var2)
if l_var % 2 != 0:
	middle = l_var // 2
	print(var2[middle])
else:
	m1 = l_var // 2
	m2 = m1 - 1
	print(var2[m2], var2[m1])"""
#Slicing
var1 = "python"
#       012345
sub_str = var1[5:1:-1] #024
# print(sub_str)
# [start:stop:step]
r_str = var1[::-1]
# print(r_str)
#.........string method.........
str1 = "pythonpppppp"
res = str1.count("p")
#print(res)
answer = input("are you student [yes, no]: ").lower()
#answer = answer.lower() #yes
"""if answer == "yes":
	print("ok")
elif answer == "no":
	print("you can't")
else:
	print("not found!")"""
#str1 = "Python"
#str1 = str1.upper()
#str1 = str1.lower()
#print(str1)