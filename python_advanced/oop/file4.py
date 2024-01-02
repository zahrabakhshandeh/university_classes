from abc import ABC, abstractmethod

class Person(ABC):
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

	@abstractmethod
	def show_info(self):
		pass


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

	def show_info(self):
		print(f"{self.name} is a student!")

	def show_id(self):
		print(self.id_)



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

	def show_info(self):
		print(f"{self.name} is a teacher!")

	def show_id(self):
		print("teacher: ", self.id_)


if __name__ == "__main__":
	st1 = Student([12], "123", "a", 12)
	t1 = Teacher("1234", "t1", 19, 2)
	print(type(t1))
	st1.show_id()
	t1.show_id()