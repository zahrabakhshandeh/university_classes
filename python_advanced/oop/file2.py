class C1:
	def show_info(self):
		print("python")

class C2(C1):
	def show_info(self):
		print("java")

class C3(C2):
	pass

if __name__ == "__main__":
	obj1 = C3()
	obj1.show_info()