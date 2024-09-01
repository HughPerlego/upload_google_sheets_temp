import pytest
from helpers import read_csv  # Import your helper function here
from confest import test_file

def test_first_organisation_is_correct(test_file):
    # Arrange
    filepath = 'organisation_data.csv'
    expected_first_org = 1

    # Act
    organisation_data = read_csv(filepath)

    # Assert
    assert organisation_data['Organisation_Id'][0] == expected_first_org

def test_organisation_name_starts_correctly(test_file):
    # Arrange
    filepath = 'organisation_data.csv'
    expected_starting_letters = 'University'

    # Act
    organisation_data = read_csv(filepath)

    # Assert
    assert organisation_data.loc[0, 'Organistion_Name'][:10] == expected_starting_letters

def test_account_manager_name(test_file):
    # Arrange
    filepath = 'organisation_data.csv'
    expected_account_managers = ['Mark', 'Jess', 'Luke']

    # Act
    organisation_data = read_csv(filepath)

    # Assert
    assert organisation_data['Account_Manager'][0] in expected_account_managers

def test_account_manager_level(test_file):
    # Arrange
    filepath = 'organisation_data.csv'
    expected_account_levels = ['Senior', 'Junior']

    # Act
    organisation_data = read_csv(filepath)

    # Assert
    assert organisation_data['Account_Manager_Level'][0] in expected_account_levels


## adding additional comment 