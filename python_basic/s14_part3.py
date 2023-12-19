list1 = [12, 13, 19]
list2 = ["python", "java", "c++"]
# list3 = ["python12", "java13", "c++19"]
list3 = []
for i, v in enumerate(list1):
	res = str(v)+list2[i]
	list3.append(res)
print(list3)