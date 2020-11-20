import os

def scan_dir(dir, indent = 0):
	print('   ' * indent + os.path.basename(dir))
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path):
			print('   ' * (indent + 1) + name)
		else:
			scan_dir(path, indent + 1)

scan_dir('.')