### List
x = 5
x = 10
print(x)
# index value
price = [200, 100, 500, 300]
# index   0     1    2   3
#                -3  -2 -1
print(price)
print(type(price))
print(price[2])
print(price[0])
print(price[-1])
# slicing
print(price[:3])
#.....Reverce...........
print(price[::-1])
#print(price[5])
## add
price = [20.0, 100.5, 500, 300]
price.append(250)
print(price)
price.insert(1, 2500)
print(price)
## Edit
price[0] = 0.0
print(price)
## Remove
"""price = [20.0, 100.5, 500, 300]
# value
print("befor remove: ", price)
res = price.remove(100.5)
print(price, res)
# index
#x = price.pop(0)
#print(price, x)
del price[0:2]
print(price)
price.clear()
print(price)
del price
print(price)"""
price = [500, 20.0, 500, 100.5, 500, 300]
#price.pop(10)
#print(price)
#price.remove(2000)
#price.remove(500)
"""del_data = 300
print(price)
c = price.count(del_data)
for i in range(c):
	price.remove(del_data)
print(price)"""
### Search
price = [500, 20.0, 500, 100.5, 500, 300]
#print(price)
# in, not in
"""value = float(input("your value: "))
if value not in price:
	price.append(value)
else:
	print("exist")"""
"""if value in price:
	price.remove(value)
	print(price)
else:
	print("not found!")"""
list1 = [500, 20.0, 50]
list2 = ["python", "java"]
print(list1 + list2)
list3 = ["-", "-"] 
list3 = list3 * 20
print(list3)
print(len(list3))