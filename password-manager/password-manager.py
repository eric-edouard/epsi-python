import json

# List data model:

# credentials_test = [
# 	{'site': 'amazon', 'id': 'eric', 'password': 'azerty123'},
# 	{'site': 'cdiscount', 'id': 'eric', 'password': 'azerty123'},
# 	{'site': 'ikea', 'id': 'eric', 'password': 'azerty123'},
# 	{'site': 'theverge', 'id': 'eric', 'password': 'azerty123'},
# ]

# credentials_test[1]['password'] = "123456"

# Object-key data model:

# credentials_test = {
# 	'amazon': {'id': 'eric', 'password': 'azerty123'},
# 	'cdiscount': {'id': 'eric', 'password': 'azerty123'},
# 	'ikea': {'id': 'eric', 'password': 'azerty123'},
# 	'theverge': {'id': 'eric', 'password': 'azerty123'},
# }

# credentials_test['cdiscount']['password'] = "123456"


class FileManager:
	filename = "passwords.txt"

	def load(self):
		try:
			file = open(self.filename, "r")
			credentials = json.load(file)
			file.close()
			return credentials
		except FileNotFoundError:
			return {}

	def save(self, credentials):
		file = open(self.filename, "w")
		json.dump(credentials, file)
		file.close()


class CredentialsManager:
	def __init__(self):
		self.__file_mgr = FileManager()
		self.credentials = self.__file_mgr.load()

	def set_credential(self, site, id, password):
		self.credentials[site] = {'id': id, 'password': password}
		self.__file_mgr.save(self.credentials)

	def remove_credential(self, site):
		if (site in self.credentials):
			del self.credentials[site]
			self.__file_mgr.save(self.credentials)
			return True
		else:
			return False

	def print(self):
		if (len(self.credentials) == 0):
			print("You have no credentials saved")
			return
		for site in self.credentials:
			crendential = self.credentials[site]
			print(f"Site: {site}  /  id: {crendential['id']}  /  password: {crendential['password']}")

class Core:
	__help = "Commands:\n\n'list' to list your crendentials\n'add' to add new credentials\n'remove' to remove a credential\n"

	def __init__(self):
		self.creds_mgr = CredentialsManager()

	def run(self):
		print(self.__help)
		while True:
			user_input = input()
			print("")
			if ("help" in user_input):
				print(self.__help)
				continue
			if ("list" in user_input):
				self.creds_mgr.print()
				continue
			if ("add" in user_input):
				site =  input("Site:     ")
				id =    input("Id:       ")
				passw = input("Password: ")
				self.creds_mgr.set_credential(site, id, passw)
				self.creds_mgr.print()
				continue
			if ("remove" in user_input):
				self.creds_mgr.print()
				site = input("Which website credentials you wish to remove ? ")
				if (self.creds_mgr.remove_credential(site)):
					print(f"{site} was deleted")
				else:
					print(f"{site} does not exists")
				continue
			print(self.__help)
		

app = Core()
app.run()