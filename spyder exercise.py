# -*- coding: utf-8 -*-
"""
Created on Thu May 27 16:32:37 2021

@author: SST-LAB
"""

class Employee:
   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   def displayCount(self):
     print( f"Total Employee  {Employee.empCount}")
   def displayEmployee(self):
       print (f"Name : {self.name}  Salary:  {self.salary}")
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print (f"total Employee  { Employee.empCount}")
