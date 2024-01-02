# list
## library ===> 
# name, is_aval, field
# add, edit, remove, display, details
# get_book, return_book
# boooks ===> 10
# name ====> are not equal, len < 10
def add():
	if len(names) < 10:
		name = input("name: ")
		if name not in names:
			if len(name) < 10:
				field = input("field: ")
				names.append(name)
				fields.append(field)
				status.append(True)
				print("added!")
			else:
				print("out of range!")
		else:
			print("Exist!")
	else:
		print("Full!")


def remove(name):
	if name in names:
		i = names.index(name)
		names.pop(i)
		status.pop(i)
		fields.pop(i)
		print("removed!")
	else:
		print("not found!")

def edit(name):
	if name in names:
		new_name = input("new name: ")
		if new_name not in names:
			if len(new_name) < 10:
				new_f = input("new field: ")
				i = names.index(name)
				fields[i] = new_f
				names[i] = new_name
				print("edited!")
			else:
				print("out of range!")
		else:
			print("Exist!")
	else:
		print("not found!")


"""names = ["b1", "b2", "b3"]
status = [True, False, True]
fields = ["python", "java", "python"]"""
# flag = False
# python==math ??? False
# java == math ??? False
# python == math ??? False

#field = math
# field = python
#flag
#   0 python == python ???? True ===> b1, True ===> flag = True
#   1 java == python   ???? False
#   2  python == python ???? True  ===> b3, True
def search(field):
	flag = False
	for i, f in enumerate(fields):
		if f == field:
			print(i+1, names[i],f , status[i])
			flag = True
	if flag == False:
		print("not found!")


def details():
	number_of_books = len(names)
	print(f"number of books: {number_of_books}")
	"""a_c = 0
	for s in status:
		if s == True:
			a_c += 1"""
	a_c = sum(status)
	print(f"available books: {a_c}")
	n_a_c = number_of_books - a_c
	print(f"not available books: {n_a_c}")

def display():
	if names == []:
		print("Empty!")
	for i, n in enumerate(names):
		print(i+1, n, fields[i], status[i])

def get_book(name):
	if name in names:
		i = names.index(name)
		if status[i] == True:
			status[i] = False
			print("done!")
		else:
			print("is not available!")
	else:
		print("not found!")

def return_book(name):
	if name in names:
		i = names.index(name)
		if status[i] == False:
			status[i] = True
			print("done")
		else:
			print("is available!")
	else:
		print("not found!")

names = ["b1", "b2", "b3"] # ===> b2  ... math
status = [True, False, True] # c = 0
#         [1, 0, 1]
#           c = 1       c = 2
fields = ["python", "java", "python"]
while True:
	cmd = input("add,edit,remove,display,search,details,get,return,exit: ")
	if cmd == "add":
		add()
	elif cmd == "remove":
		name = input("name for remove: ")
		remove(name)
	elif cmd == "edit":
		name = input("name for edit: ")
		edit(name)
	elif cmd == "search":
		field = input("field: ")
		search(field)
	elif cmd == "display":
		display()
	elif cmd == "details":
		details()
	elif cmd == "get":
		name = input("name of book: ")
		get_book(name)
	elif cmd =="return":
		name = input("name: ")
		return_book(name)
	elif cmd == "exit":
		break
	else:
		print("not found!")