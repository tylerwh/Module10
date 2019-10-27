

class Invoice:
  def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address, items_with_price = ({})):
    self.invoice_id = invoice_id
    self.customer_id = customer_id
    self.last_name = last_name
    self.first_name = first_name
    self.phone_number = phone_number
    self.address = address
    self.items_with_price = items_with_price
  
  def add_item(self, dict_add):
    self.items_with_price.update(dict_add)
  
  def create_invoice(self):
    total = 0.00
    TAX_RATE = .06
    for k in self.items_with_price:
      print(f"{k}.....{self.items_with_price[k]}")

    total = sum([value for value in self.items_with_price.values()])
    tax = total * TAX_RATE
    total_with_tax = total + tax
    print(f"Tax.....{tax}")
    print(f"Total.....{total_with_tax:,.2f}")


invoice = Invoice(1, 123, 'Mouse', 'Minnie', '555-867-5309', '1313 Disneyland Dr, Anaheim, CA 92802')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()