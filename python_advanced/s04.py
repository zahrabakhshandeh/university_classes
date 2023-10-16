#......String methods....
str1 = "python-python-python"
ind = str1.rfind("c++")
#print(str1[ind])
ind = str1.rindex("python")
#print(str1[ind])
#print(ind)
# replace
new_str = str1.replace("python", "c++")
print(new_str)
i = len(str1) // 2
left_part = str1[:i+1]
left_part = left_part.replace("python", "c++")
print(left_part)
right_part = str1[i+1:]
right_part = right_part.replace("python", "js")
print(right_part)
new_str = left_part + right_part
print(new_str)
# split, join
str1 = "python js python c++ python"
res = str1.split()
print(res)
res = ['python', 'js', 'python', 'c++', 'python']
new_str = " ".join(res)
print(new_str)
# name ===> hi Sara
res = "result: {}, {}"
name = "Sara"
print("hi", name, "!")
print(f"hi {name} !") #fString
num1 = 10
num2 = 13
sum_ = num1 + num2
multi = num1 * num2
print(res.format(sum_, multi))
#print(res.format(multi))
str1 = "python-java-c++"
new_str = str1.replace("python", "")
print(new_str)
# in, not in
print("python" not in str1)