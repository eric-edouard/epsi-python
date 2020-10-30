# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ['Apples', "Oranges", 'Grapes', 'Pears']

# for fruit in fruits:
# 	print("fruit:" + fruit)


# for fruit in fruits:
# 	if fruit == 'Grapes':
# 		break
# 	print("fruit:" + fruit)

for fruit in fruits:
	if fruit == 'Grapes':
		continue
	print("fruit:" + fruit)

for i in range(len(fruits)):
	print(f'for index {i}, fruit is {fruits[i]}')

# for i in range(0, 11):
# 	print(f'Number: {i}')


# for i in range(5, 11):
# 	print(f'Number: {i}')


for i in range(11, 0, -1):
	print(f'Number: {i}')

count = 0
while count < 10:
	print(f'Count: {count}')
	count += 1