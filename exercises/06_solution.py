
"""

Exercice 06 - Sort a string

The goal of this exercise is to sort the names of the fruits in the string.
At the end of the exercise the strings should display: "Apple, Cherry, Pear, Strawberry"

"""

fruits = "Strawberry, Apple, Pear, Cherry"
fruits_list = fruits.split(", ")
fruits_list.sort()
ordered_fruits_list = ", ".join(fruits_list)
print(ordered_fruits_list)