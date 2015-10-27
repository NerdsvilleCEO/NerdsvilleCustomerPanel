import pytest
import unittest
import os
from NerdsvilleCustomerPanel.Persistence.FlatFS import FlatFS
from NerdsvilleCustomerPanel.Controls.CustomerActions import CustomerActions

class TestFlatFS(unittest.TestCase):
    def setUp(self):
        self.customer = CustomerActions().create(fname="Joshua", lname="Santos",
        hourly_rate="72.00", company_name="Nerdsville LLC", phone="9099099090")
    def test_read_empty_file(self):
        flatFS = FlatFS("Tests/Data/File")
        open("Tests/Data/File", "w")
        self.assertTrue(flatFS.get_all() == [])

    def test_read_file_with_one_entry(self):
        flatFS = FlatFS("Tests/Data/File")
        flatFS.save(self.customer)
        customerDict = self.customer.__dict__
        customerDict["id"] = '1'
        self.assertTrue(flatFS.get_all()[0] == customerDict)

    @pytest.yield_fixture(autouse=True)
    def run_around_tests(self):
        yield
        if os.path.isfile("Tests/Data/File"):
            os.remove("Tests/Data/File")
        print "I Ran"
        assert os.path.isfile("Tests/Data/File") == False

if __name__ == '__main__':
    unittest.main()
