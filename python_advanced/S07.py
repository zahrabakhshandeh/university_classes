## product manager
# limit :name 
# ..........functions...........
def add():
	name = input("product name: ")
	number = int(input(f"number of {name}: "))
	if name in products:
		ind = products.index(name)
		numbers[ind] += number
		print("added!")
	else:
		products.append(name)
		numbers.append(number)
		print("added!")

def display():
	if products:
		for i, p in enumerate(products):
			print(f"{i+1}) name: {p}, number: {numbers[i]}")
	else:
		print("Empty!")

def remove(name):
	if name in products:
		ind = products.index(name)
		#products.pop(ind)
		#numbers.pop(ind)
		products.remove(name)
		numbers.pop(ind)
		#numbers.remove(numbers[ind])
		print("removed!")
	else:
		print("not found!")

def edit(name):
	if name in products: # new_name = p6
		new_name = input("new name: ")
		if new_name not in products:
			new_num = input("number of product: ")
			ind = products.index(name)
			products[ind] = new_name
			if new_num:
				numbers[ind] = int(new_num)

			print("edited")
		else:
			print("exist!")
	else:
		print("not found!")
def search(name):
	# p
	# p.srartswith(name) is True if p start with p, else is False
	# p.endswith(name) is True if end of the p is name, else is False
	is_found = False
	for p in products:
		if name in p:
			is_found = True
			ind = products.index(p)
			print(f"name: {p}, number: {numbers[ind]}")
	if is_found == False:
		print("not found!")

def detail():
	print(f"product: {len(products)}")
	print(f"number of products: {sum(numbers)}")
	max_p = max(numbers) # 10
	ind = numbers.index(max_p) # 2
	product = products[ind] # 2 ==> p6
	print(f"max number: {max_p}, product: {product}")
#..........main..............
products = [] 
numbers = [] 
for i in range(100):
	cmd = input("add,details,display,remove,edit,search,exit: ")
	if cmd == "add":
		add()
	elif cmd == "display":
		display()
	elif cmd == "remove":
		name = input("name of product: ")
		remove(name)
	elif cmd == "edit":
		# [p1, p2, p3, p6] # name = p4
		name = input("product name: ")
		edit(name)
	elif cmd == "search":
		# ["P1", "P2", "A1"]
		name = input("name of product: ")
		search(name)
	elif cmd == "details":
		detail()
	elif cmd == "":
		continue
	elif cmd == "exit":
		break
	else:
		print(f"{cmd}:not found!")

