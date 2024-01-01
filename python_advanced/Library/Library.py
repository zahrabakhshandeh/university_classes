from employee import *
from user import *
from book import *
class Library:
	def __init__(self, name):
		self.name = name
		self.objects = {
			"users": {},
			"employees": {},
			"books": {}
		}

	def add(self, obj):
		res = type(obj).__name__
		res = res.lower()+"s"
		self.objects[res][obj.id_] = obj

	def search(self, name):
		for dict_ in self.objects.values():
			for i in dict_.values():
				if i.name == name:
					print(i)


if __name__ == "__main__":
	l1 = Library("l1")
	b1 = Book("123", "a", "f")
	u1 = User("123", "a", "b", 29)
	l1.add(b1)
	l1.add(u1)
	print(l1.objects)
	l1.search("a")
	u1.get_book(b1)
	l1.search("a")
	print(u1.books)
	u1.return_book(b1)
	print("_"*20)
	l1.search("a")
	print(u1.books)
