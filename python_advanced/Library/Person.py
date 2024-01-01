from abc import ABC, abstractmethod
class Person(ABC):
	def __init__(self, id_, name, 
		last_name, age):
		self.id_ = id_
		self.name = name
		self.last_name = last_name
		self.age = age

	def __str__(self):
		return (f"Name: {self.name},"
				f"Last Name: {self.last_name},"
				f"Age: {self.age}")

	def edit(self, new_name=None, 
		new_last_name=None, new_age=None):
		self.name = new_name or self.name
		self.last_name = new_last_name or self.last_name
		self.age = new_age or self.age

	@abstractmethod
	def des_role(self):
		pass
