from student import *
from teacher import *
class University:
	def __init__(self, name):
		self.name = name
		self.students = {}
		self.teachers = {}

	def add_student(self, obj):
		if obj.id_ not in self.students:
			self.students[obj.id_] = obj
			print("added!")
		else:
			print("exist!")
	
	def add_teacher(self, obj):
		if obj.id_ not in self.teachers:
			self.teachers[obj.id_] = obj
			print("added!")
		else:
			print("exit!")

	def remove_student(self, id_s):
		if id_s in self.students:
			self.students.pop(id_s)
			print("removed!")
		else:
			print("not found!")

	def remove_teacher(self, id_t):
		if id_t in self.teachers:
			self.teachers.pop(id_t)
			print("removed!")
		else:
			print("not found!")

if __name__ == "__main__":
	u1 = University("fasa")
	print(vars(u1))
	st1 = Student([12, 15], "s123", "Ali", 19)
	st2 = Student([3, 18, 19], "s345", "a", 17)
	#print(type(st1))
	print(u1.students)
	u1.add_student(st1)
	u1.add_student(st2)
	u1.add_student(st1)
	print(u1.students)
	for st in u1.students.values():
		print(st)
	t1 = Teacher("t123", "n1", 18, 3)
	u1.add_teacher(t1)
	print(u1.teachers)
	u1.remove_student("s123")
	print(u1.students)

