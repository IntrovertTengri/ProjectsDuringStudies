# This is a functional testing for BinaryComparison and BinaryArithmetic operation classes. 
# Coverage class will be combined with them to test the proper OperatorOverloading

import pytest
from unittest.mock import patch
from WDC.helper.operations.binary_expressions import BinaryArithmeticOperation, BinaryComparisonOperation
from WDC.core.coverage import Coverage

@pytest.fixture
def experimental_coverage_1():
    return Coverage("CoverageName1")

@pytest.fixture
def experimental_coverage_2():
    return Coverage("CoverageName2")

class TestBinaryArithmeticOperation:
    """Unit tests for the BinaryArithmeticOperation"""

    @pytest.mark.parametrize("operator", ['+', '-', '*', '/'])
    def test_binary_operation_str(self, operator, experimental_coverage_1, experimental_coverage_2):
        """Test the string representation of binary operations."""
        x = experimental_coverage_1
        y = experimental_coverage_2
        operation = BinaryArithmeticOperation(x, operator, y)
        assert str(operation) == f"({x.get_variable_name()} {operator} {y.get_variable_name()})"

    @pytest.mark.parametrize("method, operator", [
        ('__add__', '+'),
        ('__sub__', '-'),
        ('__mul__', '*'),
        ('__truediv__', '/'),
    ])
    def test_recursion(self, method, operator, experimental_coverage_1, experimental_coverage_2):
        """Test the recursion ability."""
        x = experimental_coverage_1
        y = experimental_coverage_2
        left_op = x + y
        right_op = 3
        
        with patch('WDC.helper.error_handling.type_checks.type_check_for_binary_and_numeric_operations'):
            # Create a new operation from an existing one
            new_op = getattr(left_op, method)(right_op)
            assert isinstance(new_op, BinaryArithmeticOperation)
            assert str(new_op) == f"(({x.get_variable_name()} + {y.get_variable_name()}) {operator} 3)"

    def test_type_check_failure(self):
        """Test that type checking correctly raises TypeError when invalid types are used."""
        operation = BinaryArithmeticOperation(1, '+', 2)
        invalid_right_op = '2' # An unsupported type

        with pytest.raises(TypeError):
            operation + invalid_right_op 


class TestBinaryComparisonOperation:
    """Unit tests for the BinaryArithmeticOperation"""

    @pytest.mark.parametrize("operator", ['<', '>', '=', '<=', '>=', '!=', 'and', 'or', 'xor'])
    def test_binary_operation_str(self, operator, experimental_coverage_1, experimental_coverage_2):
        """Test the string representation of binary operations."""
        x = experimental_coverage_1
        y = experimental_coverage_2
        operation = BinaryComparisonOperation(x, operator, y)
        assert str(operation) == f"({x.get_variable_name()} {operator} {y.get_variable_name()})"

    def test_type_check_failure(self, experimental_coverage_1, experimental_coverage_2):
        """Test that type checking correctly raises TypeError when invalid types are used."""
        operation = BinaryComparisonOperation(experimental_coverage_1, '<', experimental_coverage_2)
        invalid_right_op = '2' # An unsupported type

        with pytest.raises(TypeError):
            operation + invalid_right_op   