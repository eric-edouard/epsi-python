"""

In this exercise, you will have to add a special method to the class Monster so that when you print an instance
 of this class with the method print(), it displays the characteristics of this instance.

Example:

zombie = Monster(3,8,2)
print(zombie)

// console output:
Monster has an hp of 3 attack of 8 & defense of 2

"""
class Monster:
    def __init__(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def __repr__(self):
        return f"Monster has hp of {self.hp} attack of {self.attack} & defense of {self.defense}"
 
zombie = Monster(3, 8, 2)

print(zombie)
