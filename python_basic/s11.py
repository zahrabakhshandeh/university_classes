# loop
# for
# number =====> +
"""number = int(input("number: "))
sum_numbers = 0
for i in range(number+1):
	sum_numbers += i
print(sum_numbers)
# while
number = int(input("number: "))
i = 0
sum_numbers = 0
while i <= number:
	sum_numbers += i
	i += 1
print(sum_numbers)"""
"""for i in [12, 15, 18, 10]:
	print(i)

list1 = list(range(1, 10))
print(list1)
#1  1    ====> 3
#12 1-2
#123 1-3
num = int(input("number: "))
for i in range(1, num+1):
	for j in range(1, i+1):
		print(j, end="")
	print()

#p 0-0
#py 0-1
#pyt 0-2
#pyth 0-3
#pytho
#python
name = input("your str: ")
l = len(name)
for i in range(l):
	print(name[:i+1])"""
#a,o,u,i,e
"""chrs = ["a", "o", "u", "i", "e"]
name = input("str: ")
c = 0
for i in name:
	if i in chrs:
		c += 1
print(c)"""
"""num = int(input("number: "))
# 1/1 + 1/2 + ... + 1/n
result = 0
for i in range(1,num+1):
	div = 1 / i
	result += div
print(div)"""
x = 10
y = 20
tmp = x
x = y # x = 20
y = tmp # y = 20
print(x,y)
x, y = y, x
