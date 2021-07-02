# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:45:55 2021

@author: SST-LAB
"""

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
    def speak(self):
        print("I dont know what to say")
        
        
class Cat(Pet):
    def speak(self):
        print("Meow")
        
class Dog(Pet):
    def speak(self):
        print("Bark")
        
p = Pet("Tim", 8) 
p.speak()
c = Cat("Lemon", 7)
c.show()
d = Dog("Jill", 16)
d.show()       

    