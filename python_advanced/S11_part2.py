# stu_num, name, age, scores
# students = {
#      "123" : {
	
#		}	
#}
# limit ===> stu_num
# add, display, edit, remove, search, details
def change_to_list(scores):
	scores = scores.split(",")
	scores = list(map(float, scores))
	return scores

def add():
	st_num = input("student number: ")
	if st_num not in students:
		name = input("student name: ")
		age = int(input("age: "))
		scores = input("scores: ")
		scores = change_to_list(scores)
		student = {
		"name" : name,
		"age" : age,
		"scores": scores
		}
		students[st_num] = student
		print("added!")
	else:
		print("exit")

def display():
	if not students:
		print("Empty!")
	for k, stu in students.items():
		print("*"*5, k, "*"*5)
		for i, v in stu.items():
			print(f"{i}: {v}")


def edit(stu_num):
	if stu_num in students:
		new_name = input("student name: ")
		new_age = input("age: ")
		new_scores = input("scores: ")
		students[stu_num]["name"] = new_name or students[stu_num]["name"]
		students[stu_num]["age"] = int(new_age or students[stu_num]["age"])
		if new_scores != "":
			new_scores = change_to_list(new_scores)
			students[stu_num]["scores"] = new_scores
	else:
		print(f"{stu_num}: not found!")

def remove(stu_num):
	if stu_num in students:
		students.pop(stu_num)
		print("removed!")
	else:
		print(f"{stu_num}: not found!")

def search(start, end):
	for stu in students.values():
		for s in stu["scores"]:
			if start < s < end:
				for i, j in stu.items():
					print(f"{i} : {j}")
				break

def details():
	numbers_of_stu = len(students)
	print(f"number of students: {numbers_of_stu}")
	scores = []
	for stu in students.values():
		scores += stu["scores"]
	sum_scores = sum(scores)
	max_scores = max(scores)
	min_scores = min(scores)
	avg_scores = sum_scores / len(scores)
	print(sum_scores, max_scores, min_scores, avg_scores)

# ...........main..........
students = {}
for i in range(100):
	cmd = input("add/remove/dispay/edit/search/detail/exit: ")
	if cmd == "add":
		add()
	elif cmd == "remove":
		stu_num = input("student number to remove: ")
		remove(stu_num)
	elif cmd == "display":
		display()
	elif cmd == "edit":
		stu_num = input("student number to edit: ")
		edit(stu_num)
	elif cmd == "search":
		start = input("start point: ")
		end = input("end point: ")
		start = float(start or 0)
		end = float(end or 20)
		search(start, end)
	elif cmd == "detail":
		details()
	elif cmd =="exit":
		break
	elif cmd == "":
		continue
	else:
		print(f"{cmd}: not found!")
