number = 12 # int
score = 16.2 # float
valid1 = True
valid2 = False
# integer(int), float, string(str)
# boolean(bool)
x = 10
y = x
# print(x, y)
# "", ''
z = "python c java"
# print(z)
num = "123"
# type()
type_num = type(num)
#print(type_num)
## Casting
type_num = type(num)
#print(type_num)
#..........................
# convert to str ===> str()
num = False
type2 = type(num)
#print(num, type2)
num = str(num)
type2 = type(num)
#print(num, type2)
# convert to int ===> int()
var1 = "12.9"
#var1 = float(var1)
#var1 = int(var1)
var1 = int(float(var1))
type2 = type(var1)
#print(var1, type2)
# convert to float ===> float()
var2 = False
var2 = float(var2)
print(var2)
# convert to bool ===> bool()
# "", 0, 0.0, False
var1 = ""
var2 = 200
var3 = -200
var4 = 2.9
var1 = bool(var1)
var2 = bool(var2)
var3 = bool(var3)
var4 = bool(var4)
# print(var1, var2, var3, var4)
# +, *, -, /,**, %, //
# <, >, <=, >=, ==, !=  ===> bool
num1 = 10
num2 = 15
print(num1 == num2)
# and, or, not
num1 = 10
num2 = 15
num3 = 10
#print(num1 == num3 and num2 > num1)
#print(not(num1 != num3 or num2 < num1))
#print(not(False))
#...........................
# if
num1 = 120
# if False  ====> xxxxx
# if True ====> ex
if num1 > 20:
	print(num1)