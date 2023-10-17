# float, int, str, bool
# float, int
# +, -, *, /, **, //, %
num1 = 4
num2 = 2
"""print(num1 / num2) # 2.5
print(num1 ** num2) # 25
print(num1 // num2) # 2
print(num1 % num2) # 1"""
# >, <, >=, <=, ==, !=
num1 = 4
num2 = 4
"""print(num1 >= num2)
print(num1 == num2) # True
print(num1 != num2) # False"""
# and, or, not
num1 = 4
num2 = 4
num3 = 5
#          True             False
"""print(num1 == num2 and num3 < num2 and num3 > num1)
#           True
print(num1 == num2 or num3 < num2 or num3 > num1)
#                   True
print((num1 == num2 or num3 < num2) and num1 == num2 and num3 < num2)
print((num1 + num2)> num3)
print(not(num1 == num2))
print(not(True))
print(not(False))"""
# Example
num1 = "123"
num2 = "5"
#print(num1 + num2)
# Casting
# change to int ====> int()
# change str to int
"""num1 = "123"
print(type(num1))
num1 = int(num1) # 123
print(type(num1))
print(num1 + 3)"""
num1 = "123a"
#num1 = int(num1)
#print(num1)
num1 = "12.8"
#num1 = int(num1)
#print(num1)
# change float to int
num2 = 12.5
num3 = 4.0
print(int(num2))
print(int(num3))
# change bool to int
flag1 = True
flag2 = False
print(int(flag1))
print(int(flag2))
# change to float ====> float()
# change str to float
num1 = "12.8"
num1 = float(num1) # 12.8
num1 = int(num1)   # 12
#print(num1)
num1 = "12"
num1 = float(num1)
#print(num1)
num1 = "121d"
#num1 = float(num1)
#print(num1)
# change int to float
num1 = 12
num2 = 0
print(float(num1))
print(float(num2))
# change bool to float
flag1 = True
flag2 = False
print(float(flag1))
print(float(flag2))