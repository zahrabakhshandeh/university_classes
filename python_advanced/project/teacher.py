class Teacher:
	def __init__(self, id_, name, age, rank):
		self.id_ = id_
		self.name = name
		self.rank = rank
		self.age = age

	def __str__(self):
		return f"ID: {self.id_} Name:{self.name} Rank: {self.rank}"

	def edit_profile(self, name=None, age=None):
		self.name = name or self.st_name
		self.age = age or self.age
		print("Edited!") 
if __name__ == "__main__":
	t1 = Teacher("123", "T1", 12, "2")
	print(t1)
	t1.edit_profile("T2", 19)
	print(t1)