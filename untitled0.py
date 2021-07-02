# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:24:01 2021

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
        first, last, pay = emp_str.split('.')
        return   cls(first, last, pay)

emp_1 = Employee('Lola','Porter',600000)     
emp_2 = Employee('Test','User',90000)  


emp_str_1 = 'Charles-Baba-30000'
emp_str_2 = 'Femi-Polars-750000'
emp_str_3 = 'Goode-Laware-42000'



new_emp_1 = Employee.from_string(emp_str_1)
                     
                                                              


#print(emp_1.__dict__)        
#print(Employee.__dict__)  


#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

#print(Employee.num_of_emps)

#emp_1.raise_amount
#Employee.raise_amount
#print(emp_1) 
#print(emp_2)

#print(emp_1.email)
#kprint(emp_2.email)

#print(emp_1.fullname())
#print(emp_2.fullname())        

#print(emp_1.fullname())
#print(Employee.fullname(emp_1))

