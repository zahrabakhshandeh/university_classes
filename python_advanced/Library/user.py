from Person import *
class User(Person):
	def __init__(self, id_, name,last_name,age):
		super().__init__(id_, name, last_name, age)
		self.books = {}

	def get_book(self, book):
		if book.is_available:
			#self.books.append(book)
			self.books[book.id_] = book
			book.is_available = False
		else:
			print("is not available!")

	def return_book(self, book):
		if book.id_ in self.books:
			self.books.pop(book.id_)
			book.is_available = True
		else:
			print("Invalid Input!")

	def des_role(self):
		print(f"{self.name} is a user!")

if __name__ == "__main__":
	u1 = User("123", "a", "b", 29)
	print(u1)

