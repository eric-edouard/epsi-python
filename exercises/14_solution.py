"""
In this exercise you'll need to take the class NumberList created in exercise 13
 and you will need to add the class function average() which returns the average of all elements in the instance

"""

class NumberList(list):
    
	def sum(self):
		return sum(self)

	def average(self):
		return sum(self) / len(self)
 
liste = NumberList([2, 23, 4])

print(liste)
print(liste.sum())
print(liste.average())
