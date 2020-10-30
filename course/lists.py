numbers = [1, 4, 5, 2]

# fruits = ['Apples', "Oranges", 'Grapes', 'Pears']

fruits = list(('Apples', "Oranges", 'Grapes', 'Pears'))

print(len(fruits))


fruits.append('Mango')

print(fruits)

fruits.remove('Apples')

print(fruits)

fruits.insert(2, 'Apple')

print(fruits)

fruits[0] = 'Strawberry'
print(fruits)

fruits.pop(2)
print(fruits)
