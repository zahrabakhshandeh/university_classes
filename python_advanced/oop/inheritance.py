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


class Student(Person):
	def __init__(self, scores, 
		id_, name, age):
		super().__init__(id_, name, age)
		self.scores = scores

	def __str__(self):
		data = super().__str__()
		return f"{data},Scores: {self.scores}"

	def calculate_avg(self):
		sum_ = sum(self.scores)
		avg = sum_ / len(self.scores)
		self.avg = avg
		#return avg


class Teacher(Person):
	def __init__(self, id_, name, age, rank):
		super().__init__(id_, name, age)
		self.rank = rank
	
	def __str__(self):
		data = super().__str__()
		return f"{data}, Rank: {self.rank}"
	
	def edit_profile(self, name=None, 
		age=None, rank=None):
		super().edit_profile(name, age)
		self.rank = rank or self.rank

if __name__ == "__main__":
	st1 = Student([12], "123", "a", 12)
	print(vars(st1))
	print(st1)
	st1.edit_profile(name="new name")
	print(st1)