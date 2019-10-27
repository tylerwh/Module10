"""
Author: Tyler Hochstetler
The purpose of this class is to provide data for unit testing in the test.test_student.py file
"""
import math


class Student:
  """Student Class"""
  def __init__(self, lname, fname, major='', gpa=0.0):
    name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
    if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
      raise ValueError
    self.last_name = lname
    self.first_name = fname
    self.major = major
    if (math.isnan(gpa)):
      raise TypeError
    elif not (isinstance(gpa, float)):
      raise ValueError
    self.gpa = gpa
  
  def __str__(self):
    return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
