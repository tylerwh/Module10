import unittest
from class_definitions import student as s


class MyTestClass(unittest.TestCase):
  def setUp(self):
    self.student = s.Student('Test', 'Johnny')

  def tearDown(self):
    del self.student
  
  def test_object_created_required_attributes(self):
    self.assertEqual(self.student.last_name, 'Test')
    self.assertEqual(self.student.first_name, 'Johnny')

  def test_object_created_all_attributes(self):
    student = s.Student('Bright', 'Gil', 'HVAC', 3.9)
    self.assertEqual(student.last_name, 'Bright')
    self.assertEqual(student.first_name, 'Gil')
    self.assertEqual(student.major, 'HVAC')
    self.assertEqual(student.gpa, 3.9)

  def test_student_str(self):
    gil = s.Student('Bright', 'Gil', 'HVAC', 3.9)
    # print(str(gil)) # This was just to make sure it actually printed as expected
    self.assertEqual(str(gil), "Bright, Gil has major HVAC with gpa: 3.9")

  def test_object_not_created_error_last_name(self):
    with self.assertRaises(ValueError):
      t = s.Student('321', 'Jimmy')

  def test_object_not_created_error_first_name(self):
    with self.assertRaises(ValueError):
      t = s.Student('Good', '987')

  def test_object_not_created_error_major(self):
    with self.assertRaises(ValueError):
      t = s.Student('Good', 'Jimmy', '!Communication')

  def test_object_not_created_error_gpa(self):
    with self.assertRaises(TypeError):
      t = s.Student('Phillips', 'Phil', 'CSI', 'A')
    # with self.assertRaises(ValueError):
    #   u = s.Student('Doe', 'Jane', 'Tech', -1)
    # with self.assertRaises(ValueError):
    #   v = s.Student('Marsh', 'Slug', 'Diesel', 4.1)
  
  def test_object_not_created_error_gpa_with_int(self):
    with self.assertRaises(ValueError):
      u = s.Student('Doe', 'Jane', 'Tech', -1)

if __name__ == "__main__":
  unittest.main()