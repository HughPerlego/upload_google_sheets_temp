import csv
import os
import pytest

@pytest.fixture(scope="module")
def test_file():
    with open('organisation_data.csv', 'w', newline='') as test_file:
        fieldnames = ['Organisation_Id', 'Organistion_Name', 'Account_Manager', 'Account_Manager_Level']
        stock_writer = csv.DictWriter(test_file, fieldnames=fieldnames)
        stock_writer.writeheader()
        stock_writer.writerow({'Organisation_Id' : '1', 'Organistion_Name' : 'University of Exeter',
                               'Account_Manager' : "Luke", 'Account_Manager_Level' : 'Senior'})
        stock_writer.writerow({'Organisation_Id' : '2', 'Organistion_Name' : 'University of York',
                               'Account_Manager' : "Jess", 'Account_Manager_Level' : 'Junior'})
        stock_writer.writerow({'Organisation_Id' : '3', 'Organistion_Name' : 'University of Kent',
                               'Account_Manager' : "Mark", 'Account_Manager_Level' : 'Junior'})
    yield
    os.remove('organisation_data.csv')

