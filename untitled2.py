# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:30:39 2021

@author: SST-LAB
"""

class Employee:
    
    
    num_of_emps = 0
    raise_amount = 1.5
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@campany.com'
    
        Employee.num_of_emps += 1  
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return   cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 




emp_1 = Employee('Lola','Porter',600000)     
emp_2 = Employee('Test','User',90000)
 

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))