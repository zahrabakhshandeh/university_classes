# add
"""list1 = [12, 15, 16, 18, 20]
list1.append(200)
list1.insert(2, 100)
print(list1)
# edit
list1 = [12, 15, 16, 18, 20]
list1[1] = 500
print(list1)
# remove
list1 = [20, 12, 20, 15, 16, 18, 20]
## index
x = list1.pop(2)
print(list1, x)"""
## value
#x = list1.remove(20)
#print(list1, x)
"""del list1[0:3]
print(list1)
list1.clear()
print(list1)
del list1
print(list1)"""
# search ====> in, not in
"""list1 = [12, 15, 16, 18, 20]
if 12 in list1:
	print("Yes")
num = int(input("number: "))
if num not in list1:
	list1.append(num)
else:
	list1.remove(num)
print(list1)"""
# +, *
"""list1 = [12, 15, 16]
list2 = [4, 17, 20]
list3 = list1 + list2
print(list3)
list4 = list2 * 3
print(list4)"""
## for
"""list1 = [12, 15, 16, 18, 20]
for i in list1:
	print(i)
result = list(range(1000))
print(result)"""
list1 = [12, 16, 18, 20]
for i in list1:
	print(i)
for i in range(len(list1)):
	print(i)
for i, v in enumerate(list1):
	print(i, v)
# method 
list1 = [12, 16, 12, 20]
# index
i = list1.index(12)
print(i)
c = list1.count(120)
print(c)