import datetime

class Employee:
  '''Employee Class'''
  #Constructor
  def __init__(self, lname, fname, addy, phone_num, salaried, startdate, salary):
    self.last_name = lname
    self.first_name = fname
    self.address = addy
    self.phone_number = phone_num
    self.salaried = salaried
    self.start_date = startdate
    self.salary = salary
  
  def set_last_name(self, lname):
    self.last_name = lname
  
  def set_first_name(self, fname):
    self.first_name = fname
  
  def display(self):
    pay_type = 'Hourly'
    frequency = 'hour'
    if self.salaried: 
      pay_type = 'Salaried'
      frequency = 'year'

    crafted_addy = ''
    word_count = 0
    for word in self.address.split():
      word_count += 1
      crafted_addy = crafted_addy + str(word) + ' '
      if word_count == 3:
        crafted_addy += '\n'


    # return str(self.first_name) + ' ' + str(self.last_name) + '\n' + str(crafted_addy) + '\n' + str(pay_type) + ' employee: $ f'{self.salary:.2d}'' + '/' + str(frequency) + '\n' + 'Start Date: ' + str(self.start_date)

    return f"{self.first_name} {self.last_name} \n{crafted_addy} \n{pay_type} employee: {self.salary:,.2f}/{frequency} \nStart Date: {self.start_date}"