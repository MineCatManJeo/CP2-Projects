# This is jnjnjvnjcxnvkjnbcxv classes and objects

# What is a class in python
# -- Blueprint for creating an object.

class pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nHealth: {self.hp}\nAttack: {self.dmg}"

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f"{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp if opponent.hp > 0 else 0} hp.")
            if opponent.hp > 0:
                self.hp -= opponent.dmg
                print(f"{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} now has {self.hp if self.hp > 0 else 0} hp.")
                if self.hp <= 0:
                    print(f"{self.name} has been knocked out. {opponent.name} won the battle!")
            else:
                print(f"{opponent.name} has been knocked out. {self.name} won the battle!")

bob = pokemon("Mr.Bob", "Charizard", 300, 95)
fluffy = pokemon("Fluffy", "Arcanine", 0.1, 9999999999999)

print("\033c")
print(type(9))

# Init is required to define variables

# What is an object in python
# -- An object is a specific instance on a class

# How do python classes relate to python objects
# -- A class is the creation and brain of the object, it's what makes the variables get defined and the functions run. An object is an instance of a class.

# How do you create a python class
# -- You write class and then the name of your class, then it doesn't need any parameters aside from __init__ and __str__ to complete specific tasks.

# What are methods
# -- A function that is specific to a class

# How do you createa a python object
# -- You define a variable setting it to the name of the class, with a parenthesis and the parameters for it inside the parenthesis.

# How do you call a method for an object
# Name of the object, then put a period, then put the name of the method and the parameters for it

# Why do we use python classes
# Because it organizes information better, it is more convenient, simplifies later code.