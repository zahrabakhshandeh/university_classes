from Person import *
class Employee(Person):
	def __init__(self, id_, name, last_name,age, salary):
		super().__init__(id_, name, last_name, age)
		self.salary = salary

	def __str__(self):
		data = super().__str__()
		return f"{data}, Salary: {self.salary}"

	def edit_book(self, book):
		new_name = input("new name: ")
		book.name = new_name or book.name
		new_f = input("new field: ")
		book.field = new_f or book.field

	def des_role(self):
		print(f"{self.name} is a employee!")


if __name__ == "__main__":
	e1 = Employee("123", "a", "b", 12, 1200)
	print(e1)