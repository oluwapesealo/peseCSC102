# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:37:37 2021

@author: SST-LAB
"""

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print(f"I am {self.name} and I am {se;lf.age} years old")
        
    def show(self):
        print("I dont know what to say")
        
        
class Pet(Cat):
    def show(self):
        print("Meow")
        
class Pet(Dog):
    def show(self):
        print(Bark)
        
p = Pet("Tim", 8) 
p.show()
c = Cat("Lemon", 7)
c.show
d = Dog("Jill", 16)
d.show       
    