#!/usr/bin/env python

# Create a class Puppy which takes a:
# 1. Name
# 2. Age
# 3. Weight (random, default from 10-50)
# ----Hint---- : __init__ method needed

# Create methods for the class which will:
# 1. Make the puppy name all upper case
# 2. Show the puppy's name - returns: f"The puppy's name is {<puppy name>}""

# Create a child class Leech which will inherit from parent class Puppy.

# Include another field for Leech called:
# 1. `is_hypoallergenic` - which will be a Boolean True/False
# ----Hint---- : super() method needed

# Create method for Leech:
# 1. `pet_puppy` - returns: f'You pet {<puppy's name>}!! Aww!!!'

# Make sure each class/method includes a docstring

# Make sure entire script conforms to PEP8 guidelines

# Check your work by running the script

# Standard Python Library
import random


class Puppy:

    def __init__(self, name, age, weight=random.randint(10, 50)):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        print(f"{self.name}, {self.age}, {self.weight}")

    def make_upper(self):
        return self.name.upper()

    def show_name(self):
        return f"The puppy's name is {self.name}"


class Leech(Puppy):

    def __init__(self, name, age, is_hypo=False):
        super().__init__(name=name, age=age)
        self.is_hypoallergenic = is_hypo

    def pet_puppy(self):
        return f'You pet {self.name}!! Aww!!!'


example1 = Puppy('James', 5)
example2 = Leech('Jonathan', 10, True)


if __name__ == "__main__":
    print(example1.weight)
    print('---------------------')
    print(example1.show_name())
    print('---------------------')
    print(example1.make_upper())
    print('---------------------')
    print(example2.is_hypoallergenic)
    print('---------------------')
    print(example2.make_upper())
    print('---------------------')
    print(example2.pet_puppy())
    print('---------------------')
