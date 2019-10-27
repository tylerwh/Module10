

class Customer:
  # def __init__(self, customer_id=0, last_name='', first_name='', phone_number='', address=''):
  #   self.customer_id = customer_id
  #   self.last_name = last_name
  #   self.first_name = first_name
  #   self.phone_number = phone_number
  #   self.address = address

  def __init__(self, customer_id: int = None, last_name: str = None, first_name: str = None, phone_number: str = None, address: str = None):
    self.customer_id = customer_id
    if not str(customer_id).isnumeric(): # Check to see if entry is a number
      raise AttributeError
    self.last_name = last_name
    self.first_name = first_name
    self.phone_number = phone_number
    self.address = address
  
  def display(self):
    return f"Customer Id: {self.customer_id} \nName: {self.last_name}, {self.first_name} \nPhone Number: {self.phone_number} \nAddress: {self.address}"

if __name__ == "__main__":
  cust_id = 153
  lname = "Q"
  fname = "Suzzy"
  phone_num = "555-545-4555"
  addy = "456 W Main St, Des Moines, IA"
  try:
    customer1 = Customer(cust_id, lname, fname, phone_num, addy)
    print(customer1.display())
  except AttributeError:
    print("Hey! customer_id must be a number")

  print()
  cus_id = "a23"
  name_last = "Doe"
  name_first = "Johnny"
  num_phone = "444-555-6666"
  cust_address = "321 Let's Go St, West Des Moines, IA"
  try:
    customer2 = Customer(cus_id, name_last, name_first, num_phone, cust_address)
    print(customer2.display())
  except AttributeError:
    print("Hey! customer_id must be a number")