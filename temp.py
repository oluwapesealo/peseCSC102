# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Coffee:
   coffeeCupCounter = 0
   def __init__(self, themilk, thesugar, thecoffeemate):
        self.milk = themilk
        self.sugar = thesugar
        self.coffeemate = thecoffeemate
        Coffee.coffeeCupCounter= Coffee.coffeeCupCounter +1
        print(f"you now have your coffee with {self.milk} milk, {self.sugar} sugar and {self.coffeemate} coffeemate")
        
mySugarFreeCoffee = Coffee(2,0,1)        

print(mySugarFreeCoffee.sugar)

myPlentySugarCoffee = Coffee(3,15,3)

peseFavoriteCoffee = Coffee(3,3,1)

print(myPlentySugarCoffee.sugar)

print(f"we have made {Coffee.coffeeCupCounter} coffee cups so far")\
    
print(f"we have made {mySugarFreeCoffee.coffeeCupCounter} coffee cups so far")

print(f"we have made {myPlentySugarCoffee.coffeeCupCounter} coffee cups so far")