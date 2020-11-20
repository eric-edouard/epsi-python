# A module is basically a file containing a set of functions to include in your application. 
# There are core python modules, modules you can install using the pip package manager as well as custom modules

# import datetime
from datetime import date

from camelcase import CamelCase

today = date.today()
print(today)

c = CamelCase()
print(c.hump("this is a camel case string"))