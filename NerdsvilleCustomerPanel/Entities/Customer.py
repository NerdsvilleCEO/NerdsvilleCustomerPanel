class Customer:
    def __init__(self, customer_id="", fname="", lname="", company_name="", hourly_rate="", phone=""):
        self.fname = fname
        self.lname = lname
        self.company_name = company_name
        self.hourly_rate = hourly_rate
        self.phone = phone
        self.customer_id = customer_id

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_customer_id(self):
        return self.id

    def get_hourly_rate(self):
        return self.hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate

    def set_customer_id(self, id):
        self.id = id
