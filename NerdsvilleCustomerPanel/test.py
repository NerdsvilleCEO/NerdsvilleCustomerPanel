from Controls.CustomerActions import CustomerActions
from Entities.Customer import Customer

customer = Customer(fname="Josh", lname="Santos")
customer_actions = CustomerActions()
first = raw_input("Enter the first name: ")
last = raw_input("Enter the last name: ")
customer_actions.create(fname=first, lname=last)
print customer_actions.save(1)
