
"""

Exercice 09 - Dice generator

The goal of this exercise is to generate six random numbers ranging from 1 to 6.

For example you could have:

1
4
3
5
5
2

"""

import random
 
for _ in range(6):
    nombre = random.choice(range(1, 7))
    print(nombre)