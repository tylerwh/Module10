"""
Author: Tyler Hochstetler
The purpose of this class is to provide data for unit testing in the test.test_student.py file
"""


class Student:
  """Student Class"""
  def __init__(self, lname, fname, major='', gpa=0.0):
    self.last_name = lname
    self.first_name = fname
    self.major = major
    self.gpa = gpa
  
  def __str__(self):
    return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
