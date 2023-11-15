# +, *, -
sum_nums = lambda num1, num2 : num1 + num2
multi_nums = lambda num1, num2 : num1 * num2
minus_nums = lambda num1, num2 : num1 - num2
f1 = lambda x: x + 5
list1 = ["4.4", "12", "16", "18", "20"]
# int('4')
new_list_f = list(map(float, list1))
new_list_i = list(map(int, new_list_f))
print(new_list)
#f1(6)
list2 = [4, 12, 15, 23]
new_list = list(map(f1, list2))
print(new_list)
nums1 = [3, 4, 5, 6, 4]
nums2 = [4, 5, 6, 7]
new_list = list(map(sum_nums, nums1, nums2))
print(new_list)
"""new_list = []
for i in list1:
	num = int(i)
	new_list.append(num)
print(new_list)"""
"""opr = input("+ or - or *: ")
num1 = int(input("num1: "))
num2 = int(input("num2: "))
if opr == "+":
	res = sum_nums(num1, num2)
	print(res)
elif opr == "-":
	res = minus_nums(num1, num2)
	print(res)
else:
	res = multi_nums(num1, num2)
	print(res)"""
