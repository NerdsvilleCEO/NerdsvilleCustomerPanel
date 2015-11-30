from NerdsvilleCustomerPanel.Entities.Customer import Customer
from NerdsvilleCustomerPanel.Persistence.FlatFS import FlatFS

class CustomerActions:
    def __init__(self):
        self.customer = Customer()

    def __str__(self):
        return self.customer.fname + " " + self.customer.lname

    def create(self, **kwargs):
        for attr, value in self.customer.__dict__.items():
            if kwargs.get(attr, None) != None:
                setattr(self.customer, attr, kwargs.get(attr, None))
        return self.customer

    def get_all_customers(self, method):
        if method == 1:
            return FlatFS("Customer").get_all()

    def save(self, method):
        """
          1.) Flat FS
          2.) PostgreSQL
        """
        if method == 1:
            self.customer.id = FlatFS("Customer").save(self.customer)
            return self.customer.id

    def read(self, id):
        self.customer = FlatFS("Customer").get_by_id(id)

    def update(self, method):
        if method == 1:
            return FlatFS("Customer").update(self.customer)
