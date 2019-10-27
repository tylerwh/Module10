import employee as em
import datetime

if __name__ == "__main__":
  # Sasha Patel object
  lname = 'Patel'
  fname = 'Sasha'
  addy = "123 Main Street Urbandale, Iowa"
  phone_num = "555-555-5555"
  salaried = True
  startdate = datetime.date(2019, 6, 28)
  salary = 40000
  emp = em.Employee(lname, fname, addy, phone_num, salaried, startdate, salary)

  # Tyler Hochstetler object
  lname = 'Hochstetler'
  fname = 'Tyler'
  addy = "321 Middle Street WDM, Iowa"
  phone_num = "555-555-5552"
  salaried = False
  startdate = datetime.date(2019, 2, 14)
  salary = 46
  emp1 = em.Employee(lname, fname, addy, phone_num, salaried, startdate, salary)

  print(emp.display())
  print()
  print(emp1.display())