

x = 23
y = 24

if x > y:
	print(f'{x} is greater than {y}')
else:
	print(f'{y} is greater than {x}')


if x > y:
	print(f'{x} is greater than {y}')
elif x == y:
	print("values are equal")
else:
	print(f'{y} is greater than {x}')

if x > 6:
	if x < 50:
		print(f'{x} is between 6 and 50')

if x > 6 and x < 40:
	print(f'{x} is between 6 and 40')

if x > 6 or x < 4:
	print(f'{x} is between 6 or lower than 4')

if not(x == y):
	print(f'{x} is not equal to {y}')

z = 67
numbers = [1, 2, 3, 4, 5]

# if z in numbers:
# 	print(z in numbers)

if z not in numbers:
	print(z not in numbers)

if x is y:
	print("X is equal to Y")

if x is not y:
	print("X is equal to Y")