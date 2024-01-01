class Book:
	def __init__(self, id_, name, field):
		self.id_ = id_
		self.name = name
		self.field = field
		self.is_available = True

	def __str__(self):
		return f"Name: {self.name}, is_available: {self.is_available}"


if __name__ == "__main__":
	b1 = Book("123", "a", "f")
	print(b1)
	