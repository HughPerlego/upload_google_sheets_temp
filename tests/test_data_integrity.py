import pytest
from helpers import read_csv  # Import your helper function here
from confest import test_file

def test_organisation_data_length(test_file):
    # Arrange
    filepath = 'organisation_data.csv'
    expected_length = 3

    # Act
    organisation_data = read_csv(filepath)

    # Assert
    assert len(organisation_data) == expected_length

def test_organisation_id_max_value(test_file):
    # Arrange
    filepath = 'organisation_data.csv'
    expected_maximum_value = 500

    # Act
    organisation_data = read_csv(filepath)

    # Assert
    assert organisation_data['Organisation_Id'].max() < expected_maximum_value

