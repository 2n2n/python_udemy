# class LotteryPlayer:
# 	def __init__(self):
# 		self.name = "Rolf"
# 		self.numbers = (5, 9, 12, 3, 1, 21)
# 	def total(self):
# 		return sum(self.numbers)

# player = LotteryPlayer()
# print(player.name)
# print(player.numbers)
# print(player.total())


class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks)/len(self.marks)

	@classmethod
	def go_to_school(cls, student):
		return cls(student.name+' - clone', student.school)
	
	@staticmethod
	def g_to_s(arg):
		print(arg)

anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
anna.marks.append(56)
print(anna.marks)	
print(anna.average())
clone = Student.go_to_school(anna)
print("{}, {}".format(clone.name, clone.school))
