class Student:
	def __init__(self, scores, 
		id_, name, age):
		self.id_ = id_
		self.st_name = name
		self.age = age
		self.scores = scores

	def __str__(self):
		return f"ID: {self.id_}, Name: {self.st_name}, Age: {self.age}, Scores: {self.scores}"


	def calculate_avg(self):
		sum_ = sum(self.scores)
		avg = sum_ / len(self.scores)
		self.avg = avg
		#return avg

	def edit_profile(self, name=None, age=None):
		self.st_name = name or self.st_name
		self.age = age or self.age
		print("Edited!") 

if __name__ == "__main__":
	st1 = Student([12], "123", "a", 12)
	print(st1)
	st1.edit_profile(age=17, name="Sara")
	print(st1)

