import unittest
from class_definitions import student as s


class MyTestClass(unittest.TestCase):
  def setUp(self):
    self.student = s.Student('Test', 'Johnny')

  def tearDown(self):
    del self.student
  
  def test_object_created_required_attributes(self):
    pass

  def test_object_created_all_attributes(self):
    pass

  def test_student_str(self):
    pass

  def test_object_not_created_error_last_name(self):
    pass

  def test_object_not_created_error_first_name(self):
    pass

  def test_object_not_created_error_major(self):
    pass

  def test_object_not_created_error_gpa(self):
    pass

if __name__ == "__main__":
  unittest.main()