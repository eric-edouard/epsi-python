# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json
import tree

# userJSON = '{"first_name": "Eric", "last_name" : "Amilhat", "city": "Toulouse"}'

# user = json.loads(userJSON)
# user['first_name'] = "test"
# print(user)

# animal = {
# 	'type': 'lion',
# 	'age': 6
# }

# animalJSON = json.dumps(animal)

# file = open("data.txt", "w")
# file.write(animalJSON)
# file.close
# print(animalJSON)

file = open("data.txt", "r")
text = file.read()
data = json.loads(text)
data['age'] = 10
print(data)