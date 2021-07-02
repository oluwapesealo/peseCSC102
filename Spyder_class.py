# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:17:10 2021

@author: SST-LAB
"""

class XBank:
    loggedinCounter = 0
    def __init__(self,theatmpin, theaccountbalance, thename):
        self.atmpin = theatmpin
        self.accountbalance = theaccountbalance
        self.name = thename
        XBank.loggedinCounter = XBank.loggedinCounter + 1
    def CollectMoney(self, amounttowithdraw):
        if(amounttowithdraw > self.accountbalance):
            print("Sorry we are not able to process at this time")
        else:
            print("Collect your cash...Thanks for banking with Xbank")
    def ChangePin(self, newpin):
        self.atmpin = newpin
        print("Your Pin has been changed...Thanks for banking with Xbank")
    @classmethod
    def NoOfCustomersLoggedIn(cls):
        print("We have a total of" + str(XBank.loggedinCounter) + "that have logged in")
f = open("C:\\Users\\SST-LAB\\Desktop\\database.txt",'r')
#print(f.readline())
password = []
accountB = []
name = []
breaker = []
for x in f:
    breaker = x.split(" ")
    password.append(breaker[0])
    accountB.append(breaker[1])
    name.append(breaker[2])
    break
    
print("enter your pin......")

pasw = input()

if (pasw ==password[0]):

    customer = XBank(password[0], accountB[0], name[0])
else:
    print("sorry your password does not match")