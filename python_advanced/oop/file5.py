# public ===> all
# protected ===> parent and child
# private ===> only class
class Student:
	def __init__(self, scores, 
		id_, name, age):
		self.__id_ = id_
		self.scores = scores
		self.name =name
		self._age = age

	def __str__(self):
		return f"Name: {self.name},Scores: {self.scores}"

	def calculate_avg(self):
		sum_ = sum(self.scores)
		avg = sum_ / len(self.scores)
		self.avg = avg
		#return avg

	def __show_info(self):
		print(f"{self.name} is a student!")

	@property
	def id_(self):
		return self.__id_

	@id_.setter
	def id_(self, new_id):
		self.__id_ = new_id

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, new_age):
		self._age = new_age

if __name__ == "__main__":
	st1 = Student([16, 17], "123", "st1", 20)
	print(st1._Student__id_)  #getter
	st1._Student__id_ = "12345" #setter
	#st1.__show_info()
	print(vars(st1))
	print(st1.id_)
	st1.id_ = "345S"
	print(st1.id_)
	print(st1.age)
	st1.age = 28
	print(st1.age)

	