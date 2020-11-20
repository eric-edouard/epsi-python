"""
In this exercise, you need to create a class NumberList that inherits from the Python list class.

This class shall have a method sum() which takes no parameters and returns the sum of all the elements in the list
"""

class NumberList(list):
    
	def sum(self):
		return sum(self)
 
liste = NumberList([2, 23, 4])

print(liste)
print(liste.sum())
