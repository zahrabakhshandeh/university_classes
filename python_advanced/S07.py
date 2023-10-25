## product manager
# limit :name 
products = [] 
numbers = [] 
for i in range(100):
	cmd = input("add,details,display,remove,edit,search,exit: ")
	if cmd == "add":
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
	elif cmd == "display":
		if products:
			for i, p in enumerate(products):
				print(f"{i+1}) name: {p}, number: {numbers[i]}")
		else:
			print("Empty!")
	elif cmd == "remove":
		name = input("name of product: ")
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
	elif cmd == "edit":
		# [p1, p2, p3, p6] # name = p4
		name = input("product name: ")
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
	elif cmd == "search":
		# ["P1", "P2", "A1"]
		name = input("name of product: ")
		is_found = False
		for p in products:
			if name in p:
				is_found = True
				ind = products.index(p)
				print(f"name: {p}, number: {numbers[ind]}")
		if is_found == False:
			print("not found!")
	elif cmd == "details":
		print(f"product: {len(products)}")
		print(f"number of products: {sum(numbers)}")
		max_p = max(numbers) # 10
		ind = numbers.index(max_p) # 2
		product = products[ind] # 2 ==> p6
		print(f"max number: {max_p}, product: {product}")
	elif cmd == "":
		continue
	elif cmd == "exit":
		break
	else:
		print(f"{cmd}:not found!")

