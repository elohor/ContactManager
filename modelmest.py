class School:
	def __init__(self, eits, fellows):
		self.eits = eits
		self.fellows = fellows

	# def add_eit(self, eit):
	# 	self.eits.append(fellow)

	# def add_fellow(self, fellow):
	# 	self.fellows.append(fellow)

class Person:
	def __init__(self, names, nationality):
		self.names = names
		self.nationality = nationality


class Eit(Person):
	def __init__(self, names, nationality):
		super().__init__(names, nationality)

	def fun_facts(self, string = ""):
		print (string)


class Fellow(Person):
	def __init__(self, names, nationality, happiness_level):
		super().__init__(names, nationality)
		self.happiness_level = happiness_level
		
	def eat(self, food, happiness_level = 1):
		self.happiness_level += happiness_level 
		print ("I ate {} today and my happiness level increased to {}".format(food,self.happiness_level))

	def teach(self, subject, happiness_level = 1):
		self.happiness_level -= happiness_level 
		print ("I taught {} today and my happiness level decreased to {}".format(subject,self.happiness_level))


if __name__ == "__main__":
	Andrew = Fellow("Andrew", "American", 5)
	Francis = Fellow("Francis", "Ghanian", 5)
	Elohor = Eit("Elohor", "Nigerian")
	Simon = Eit("Simon", "Ghanian")
	Kelvin = Eit("Kelvin", "Ghanian")
	Andrew.eat("banku", 7)

	# add_eit(School(Andrew, Elohor))
	# add_fellow(School(Francis, kelvin))
