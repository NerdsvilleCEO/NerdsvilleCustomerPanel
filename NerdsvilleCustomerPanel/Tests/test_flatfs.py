import pytest
import unittest
import os, sys
from NerdsvilleCustomerPanel.Persistence.FlatFS import FlatFS
from NerdsvilleCustomerPanel.Controls.CustomerActions import CustomerActions

class TestFlatFS(unittest.TestCase):
    def setUp(self):
        self.customers = [
            CustomerActions().create(fname="Joshua", lname="Santos",
                hourly_rate="72.00", company_name="Nerdsville LLC", phone="9099099090"),
            CustomerActions().create(fname="Test", lname="Test1",
                hourly_rate="8.00", company_name="Test", phone="1231231231")
        ]
        for customer in self.customers:
            customer.__dict__.pop("customer_id", None)

    def test_read_empty_file(self):
        flatFS = FlatFS("Tests/Data/File")
        open("Tests/Data/File", "w")
        self.assertTrue(flatFS.get_all() == [])

    def test_read_file_with_one_entry(self):
        flatFS = FlatFS("Tests/Data/File")
        self.customers[0].id = flatFS.save(self.customers[0])
        customerDict = self.customers[0].__dict__
        print customerDict
        print flatFS.get_all()[0]
        self.assertTrue(flatFS.get_all()[0] == customerDict)

    def test_read_file_by_id(self):
        flatFS = FlatFS("Tests/Data/File")
        for key, customer in enumerate(self.customers):
            self.customers[key].id = flatFS.save(customer)
        print self.customers[1].__dict__
        print flatFS.get_by_id(2)
        self.assertTrue(flatFS.get_by_id(2) == self.customers[1].__dict__)

    @pytest.yield_fixture(autouse=True)
    def run_around_tests(self):
        yield
        if os.path.isfile("Tests/Data/File"):
            os.remove("Tests/Data/File")
        print "I Ran"
        assert os.path.isfile("Tests/Data/File") == False

if __name__ == '__main__':
    unittest.main()
