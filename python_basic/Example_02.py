#limit1: number of students ===> <= 10
# limit2: student numbers are not equal
# limit3: scores between 0 and 20
# limit4: length of student numbers are 4 and start with "s"
# add ===> all of them (st_num, score)
# remove ===> (st_num)
# edit ===> limit3 (st_num, new_score)
# search ===> (st_num)
# display ====>
# details ====> 
def add():
	if len(students) >= 10:
		print("can not add!")
		return
	st_num = input("student number: ")
	if st_num not in students:
		if len(st_num) == 4  and st_num[0] == "s":
			score = float(input("your score: "))
			if score >= 0 and score <= 20:
				students[st_num] = score
				print("added!")
			else:
				print("invalid score!")
		else:
			print("invalid!")
	else:
		print("exist!")

def remove(st_num):
	if st_num in students:
		students.pop(st_num)
		print("removed!")
	else:
		print("not found!")

def edit(st_num):
	if st_num in students:
		new_score = float(input("new score: "))
		if new_score >= 0 and new_score <= 20:
			students[st_num] = new_score
			print("edited!")
		else:
			print("invalid score!")
	else:
		print("not found!")

def search(st_num):
	if st_num in students:
		print(students[st_num])
	else:
		print("not found!")

def display():
	for k, v in students.items():
		print(f"{k} ----> {v}")

def details():
	number_of_students = len(students)
	print(f"number of students: {number_of_students}")
	scores = students.values()
	max_score = max(scores)
	print(f"max scores: {max_score}")
	min_score = min(scores)
	avg = sum(scores) / number_of_students
	print(f"min scores: {min_score}")
	print(f"avg: {avg}")

students = {}
while True:
	cmd = input("add, edit, remove, search, details, display, exit: ")
	if cmd == "add":
		add()
	elif cmd == "edit":
		st_num = input("student number: ")
		edit(st_num)
	elif cmd == "remove":
		st_num = input("student number: ")
		remove(st_num)
	elif cmd == "search":
		st_num = input("student number: ")
		search(st_num)
	elif cmd == "display":
		display()
	elif cmd == "details":
		details()
	elif cmd == "exit":
		break
	else:
		print("not found!")




