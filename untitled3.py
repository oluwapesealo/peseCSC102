# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:44:43 2021

@author: SST-LAB
"""

class Student:
     studentLevel = 'first year computer science 2020/2021 session'
     studentCounter = 0
     registeredCourse = 'CSC 102'
     def __init__(self, thename, thematricno, thesex, thehostelname, theage, thecsc102examscore):
         self.name = thename
         self.matricno = thematricno
         self.sex = thesex
         self.hostelname = thehostelname
         self.age = theage
         self.csc102examscore = thecsc102examscore
         Student.studentCounter = Student.studentCounter

     def getName(self):
         return  self.name

     def setName(self, thenewName):
         self.name = thenewName
     def studentage(name, age):
         if age > 16:
             print(name, 'is greater than 16')

     @staticmethod
     def PAUNanthem():
        print('Pau, here we come, Pau, here we come ')
     @classmethod
     def course(cls):
         print('The registered course is', cls.registeredCourse)
Student.PAUNanthem()
#studendt1 = Student('James Kaka', '021074', 'M')
#print(studendt1.getName())
#studendt1.setName('James Gaga')
#print(studendt1.getName())


   # def __init__(self, csc102):
    #    self.csc102 = csc102
        
Student.course()