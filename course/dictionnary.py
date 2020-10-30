# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create a dictionnary
pet = {
	'name': 'Bus',
	'type': 'Dog',
	'age': 8,
	'is_good_boy': True
}

print(pet)


print(pet)

print(pet.keys())

print(pet.values())

pet2 = pet.copy()

pet2['height'] = 56

print(pet)

print(pet2)

del(pet['name'])

print(pet)

pet.clear()

print(pet)