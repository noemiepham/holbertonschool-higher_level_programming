#!/usr/bin/python3

class Person:
  def __init__(self):
    self.__age = 20


  def showAge(self):
      print(self.age)

  def setAge(self, age):
      self.age = age
  # private method
  def info():
    print("Info of a person.")

david = Person()
# AttributeError: 'Person' object has no attribute '__age'
print(david.__age)
