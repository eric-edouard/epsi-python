# A class is like a blueprint for creating objects. 
# An object has properties and methods(functions) associated with it. Almost everything in Python is an object


class Animal:
	# constructor
	def __init__(self, species, height, age):
		self.species = species
		self.height = height
		self.age = age

		# varible encapsulation: declared with "_"
		self._legs = 4

	def greet(self):
		print(f"I am a {self.species}, I am {self.height}cm tall and I am {self.age} years old.")

	def get_number_of_legs(self):
		return self._legs

class Insect(Animal):
	# constructor
	def __init__(self, species, height, age):
		Animal(species, height, age)
		self.species = species
		self.height = height
		self.age = age

		self.has_antennas = False
	
	def greet(self):
		print(f"I am a {self.species}, I am {self.height}cm tall and I am {self.age} years old. Do I have antennas ? {self.has_antennas}")

	def set_has_antennas(self, value):
		self.has_antennas = value

ant = Insect("ant", 120, 4)

ant.set_has_antennas(True)
ant.greet()


