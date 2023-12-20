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

st1 = Student([12, 15], "123", "a", 17)
st2 = Student([12, 16], "1234", "b", 17)
print(st1)
print(st2)
res = st2.calculate_avg()
#dir
#vars
print(vars(st1))
st1.calculate_avg()
print(vars(st1))
