# tuple
# set
"""names = ("python", "java", "c")
print(type(names))
print(names[0:2])
print(len(names))
t1 = ()
t2 = tuple()
print(type(t1))
t3 = (12,)
print(type(t3))
# add
t1 = (12, 13, 14, 14, 17)
t1 = list(t1)
print(t1)
t1.append(20)
print(t1)
t1 = tuple(t1)
print(t1)"""
#t1[2] = 2000
def test(x, y):
	res1 = x * y
	res2 = x + y
	return res1, res2

res1, res2 = test(3, 17)
print(res1, res2)
x, *_, z = (12, 14, 16, 3, 16)
print(x, z)

# Set
set1 = {12, 13, 12, 16, 17}
print(set1)
for i in set1:
	print(i)

set1.add(30)
print(set1)
set1.pop()
set1.remove(30)
#del set1
#set1.clear()
print(set1)
str1 = "I am learning python. I Love python!"
ignore = (".", "!", "_")
for i in ignore:
	str1 = str1.replace(i, "")
data = str1.split()
data1 = set(data)
print(data1)
for i in data1:
	print(i, str1.count(i))