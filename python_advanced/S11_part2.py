# stu_num, name, age, scores
# limit ===> stu_num
# add, display, edit, remove, search, details
def add():
	st_num = input("student number: ")
	if st_num not in students:
		name = input("student name: ")
		age = int(input("age: "))
		scores = input("scores: ")
		scores = scores.split(",")
		scores = list(map(float, scores))
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


def edit():
	pass

def remove():
	pass

def search():
	pass

def details():
	pass

# ...........main..........
students = {}
for i in range(100):
	cmd = input("add/remove/dispay/edit/search/detail/exit: ")
	if cmd == "add":
		add()
	elif cmd == "remove":
		remove()
	elif cmd == "display":
		display()
	elif cmd == "edit":
		edit()
	elif cmd == "search":
		search()
	elif cmd == "detail":
		details()
	elif cmd =="exit":
		break
	elif cmd == "":
		continue
	else:
		print(f"{cmd}: not found!")
