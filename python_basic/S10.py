# ToDoList
# add, edit, remove, search, detail
# ["hw", "pyython", "java"]
# [True, True, False]
# limit ====> task
# hw
list_task = ["hw1", "hw2", "python"]
list_status = []
while True:
	cmd = input("add,done, display, remove, edit, search, detail, exit: ")
	if cmd == "add":
		task = input("your task: ")
		if task not in list_task:
			list_task.append(task)
			list_status.append(False)
			print("added!")
		else:
			print("Exist!")
	elif cmd == "remove":
		task = input("your task to remove: ")
		if task in list_task:
			i = list_task.index(task)
			#list_task.remove(task)
			list_task.pop(i)
			list_status.pop(i)
			print("removed!")
		else:
			print(f"{task}: not found!")
	elif cmd == "display":
		if len(list_task) == 0:
			print("Empty!")
		for i, t in enumerate(list_task):
			print(f"{i+1}: {t} ----> {list_status[i]}")
	elif cmd == "edit":
		task = input("your task to edit: ")
		if task in list_task:
			new_task = input("new task: ")
			if new_task not in list_task:
				i = list_task.index(task)
				list_task[i] = new_task
				print("edited!")
			else:
				print("Exist!")
		else:
			print(f"{task}: not found!")
	elif cmd == "search":
		task = input("your task to search: ") #task = hw
		for t in tasks: # t = hw1
			if task in t: # if hw in hw1
				i = list_task.index(task)
				print(f"{task} ---> {list_status[i]}")
			
	elif cmd == "done":
		task = input("your task: ")
		if task in list_task:
			i = list_task.index(task)
			list_status[i] = True
		else:
			print(f"{task}: not found!")
	elif cmd == "detail":
		number_of_tasks = len(list_task)
		print(f"number of your task= {number_of_tasks}")
	elif cmd == "":
		continue
	elif cmd == "exit":
		break
	else:
		print(f"{cmd}: not found!")

