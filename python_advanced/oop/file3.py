class Person:
	def __init__(self, id_, name, age):
		self.id_ = id_
		self.name = name
		self.age = age

	def __str__(self):
		return f"ID: {self.id_}, Name: {self.name}, Age: {self.age}"

	def edit_profile(self, name=None, age=None):
		self.name = name or self.name
		self.age = age or self.age
		print("Edited!") 

class University:
	def __init__(self, name):
		self.name = name
		self.var1 = "new"


class Teacher(Person, University):
	def __init__(self, id_,
	 name, age, rank):
		Person.__init__(self, id_, name, age)
		University.__init__(self, "test")
		self.rank = rank
	
	def __str__(self):
		data = super().__str__()
		return f"{self.var1},{data}, Rank: {self.rank}"
	
	def edit_profile(self, name=None, 
		age=None, rank=None):
		super().edit_profile(name, age)
		self.rank = rank or self.rank

if __name__ == "__main__":
	t1 = Teacher("123", "t1", 28, 3)
	print(t1)