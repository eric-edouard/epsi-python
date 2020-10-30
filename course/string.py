# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

city = 'toulouse'
temperature = 16

# Concatenate
print('You are in ' + city + ' and it\'s currenlty ' + str(temperature))

# Arguments by position
print('You are in {city} and it\'s currenlty {temperature}'.format(city=city, temperature=temperature))

# F-Strings (3.6+)
print(f'You are in {city} and it\'s currenlty {temperature}')

print(city.capitalize())

print(city.upper())

print(city.lower())

print(len(city))