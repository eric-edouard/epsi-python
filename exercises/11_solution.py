"""

Using the class in exercise 10 you will have to add three attributes : hp, attack and defense.
You'll also have to initialise the instance zombie of the class monster with the following characteristics
    hp = 3
    attack = 8
    defense = 2

⚠️  This means that you'll need to create a method to initialise the instance

You cannot simply modify the attributes of the instance to give them different values.

Finally you'll have to create a method "print_infos" which doesn't take any parameters 
and will print the characteristics of the instance (hp, attack & defense) 

"""

class Monster:    
    def __init__(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def print_infos(self):
        print("Monster has hp of " + str(self.hp) + " attack of " + str(self.attack) + " & defense of " + str(self.defense)) 

zombie = Monster(3, 8, 2)

zombie.print_infos()
