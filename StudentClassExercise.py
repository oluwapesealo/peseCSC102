# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 16:09:20 2021

@author: SST-LAB
"""

class Student:
     studentLevel = 'first year computer science 2020/2021 session'
     studentCounter = 0
     def __init__(self, thename, thematricno, thesex, thehostelname, theage, thecsc102examscore):
         self.name = thename
         self.matricno = thematricno
         self.sex = thesex
         self.hostelname = the hostelname
         self.age = theage
         self.csc102examscore
         Student.studentCounter = Student.studentCounter

     def getName(self):
         return  self.name
     
     def studentage(name, age):
         if age > 16:
             print(name, is above 16)
            

     def setName(self, thenewName):
         self.name = thenewName

     @staticmethod
     def PAUNanthem():
        print('Pau, here we come, Pau, here we come ')

studendt1 = Student('James Kaka', '021074', 'M')
print(studendt1.getName())
studendt1.setName('James Gaga')
print(studendt1.getName())

Student.PAUNanthem()
    registeredCourse ='computer science 2020/2021'
    def __init__(self, thecsc102):
        self.csc102 = csc102
        
    @classmethod
    def info(cls):
        return cls.registeredCourse
print(Student.info)