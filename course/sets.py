# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits = {'Apples', 'Oranges', 'Grapes'}

print('Apples' in fruits)

fruits.add('Pears')
fruits.add('Pears')
fruits.add('Pears')

print(fruits)

fruits.remove('Grapes')

print(fruits)

fruits.clear()

print(fruits)

del fruits

print(fruits)
