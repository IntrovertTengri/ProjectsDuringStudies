# here you can find unit tests for type checkers
import pytest
from WDC.helper.error_handling.type_checks import is_string, is_list_of_strings, type_check_subset
from WDC.helper.error_handling.type_checks import data_format_exists


class TestIsString:
    """Unit tests for is_string() method"""

    def test_input_value_is_not_string(self):
        input_value = 2
        with pytest.raises(TypeError):
            is_string(input_value)


class TestIsListOfStrings:
    """Unit tests for is_list_of_strings() method"""

    def test_input_value_is_not_list(self):
        """Argument is not a list"""
        input_value = 2
        with pytest.raises(TypeError):
            is_list_of_strings(input_value)

    def test_input_value_is_not_list_of_strings(self):
        """Argument is not a list of strings"""
        input_value = ['my_string', 'another_string', 2]
        with pytest.raises(TypeError):
            is_list_of_strings(input_value)


class TestTypeCheckSubset:
    """Unit tests for type_check_subset"""

    def test_input_value_is_not_allowed(self):
        """Argument's class is not allowed"""
        input_value = True
        with pytest.raises(TypeError):
            type_check_subset(input_value)


class TestReturnFormat:
    """ Unit test for data_format_exists"""

    def test_format_is_not_allowed(self):
        """ format isn't in allowed list of return formats"""
        input_value = "not_available"
        with pytest.raises(KeyError):
            data_format_exists(input_value)
