scores = {
	"s99123" : 12,
	"s99167" : 14,
	"s98654" : 12.7
} 
for i, j in scores.items():
	print(i, j)

# remove
scores.popitem()
print(scores)
"""scores.pop("s99123")
print(scores)
del scores["s98654"]
print(scores)
#del scores
scores.clear()
print(scores)"""

# stu_num, name, age, scores
# limit ===> stu_num
students = {
	"S123":{
		"name":"A",
		"age":18,
		"scores":{
			"math":17,
			"python":13
		}
	},
	"S143":{
		"name":"B",
		"age":18,
		"scores":[12, 15]
	}
}
print(students["S123"]["scores"][1])
s1 = {
	"stu_num":"S123",
	"name":"A",
	"age":19,
	"scores":[12, 15]
}
s2 = {
	"stu_num":"S153",
	"name":"A",
	"age":19,
	"scores":[12, 15]
}
students = [s1, s2]
print(students[1])