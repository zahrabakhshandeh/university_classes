# dictionary
scores = [12, 14, 12.7]
# index - value ===> list
# key - value  ===> dict
# item ==> (key, value)
scores = {
	"s99123" : 12,
	"s99167" : 14,
	"s98654" : 12.7
}
print(scores["s99123"])
student = {
	"name" : "a",
	"age" : 19,
	"math_score" : 17,
	"python_score" : 19,
	"st_num" : "s1234"
} 
#print(student)
new_dict = {}
new_dict = dict()
# length ===> len()
print(len(new_dict))
# add
student = {
	"st_num" : "s1234"
} 
student.update({"name":"gh", "age":30})
print(student)
student["python_score"] = 19
# edit
student = {
	"name" : "a",
	"age" : 19,
	"math_score" : 17,
	"python_score" : 19,
	"st_num" : "s1234"
} 
student["name"] = "gh"
#print(student)
student.update({"age":23, "java_score":19})
print(student)
# search ===> in, not in
scores = {
	"s99123" : 12,
	"s99167" : 14,
	"s98654" : 12.7
} 
st_nums = list(scores.keys())
print(st_nums)
st_scores = list(scores.values())
print(st_scores)
st_items = list(scores.items())
print(st_items)
if ("s99123", 12) in st_items:
	print("yes")

if "s99123" in scores:
	print("yes, we have it")
