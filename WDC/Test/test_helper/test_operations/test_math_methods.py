# unit testing for MathOperation

import pytest
from unittest.mock import patch
from WDC.helper.operations.numoperations import MathOperation
from WDC.core.coverage import Coverage


@pytest.fixture
def simple_expression():
    coverage = Coverage("CoverageName")
    return (coverage / 2)


class TestMathOperation:
    """Unit tests for the MathOperation class."""

    def test_initialization_and_str(self, simple_expression):
        """Test initialization and string representation."""
        op = MathOperation('round', simple_expression)
        assert op.operation == 'round'
        assert str(op.expression) == str(simple_expression)
        assert str(op) == f'round({simple_expression})'

    @pytest.mark.parametrize("method, operation", [
        ('round', 'round'),
        ('abs', 'abs'),
        ('floor', 'floor'),
        ('ceil', 'ceil'),
        ('exp', 'exp')
    ])
    def test_unary_operations(self, method, operation, simple_expression):
        """Test unary mathematical operation methods."""
        with patch('WDC.helper.error_handling.type_checks.type_check_for_binary_and_numeric_operations'):
            operation_class = getattr(MathOperation, method)
            result = operation_class(simple_expression)
            assert isinstance(result, MathOperation)
            assert str(result.operation) == operation
            assert str(result.expression) == str(simple_expression)
            assert str(result) == str(f'{method}({simple_expression})')

    @pytest.mark.parametrize("method, operation", [
        ('mod', 'mod'),
        ('log', 'log'),
        ('pow', 'pow'),
        ('atan2', 'atan2')
    ])
    def test_binary_operations(self, method, operation, simple_expression):
        """Test binary arithmetic operation methods."""
        expected_expr = f'{method}({simple_expression}, 2)'
        with patch('WDC.helper.error_handling.type_checks.type_check_for_binary_and_numeric_operations'):
            operation_class = getattr(MathOperation, method)
            result = operation_class(simple_expression, 2)
            assert isinstance(result, MathOperation)
            assert str(result.operation) == str(operation)
            assert str(result.expression) == f'{simple_expression}, 2'
            assert str(result) == expected_expr

    def test_incorrect_type_check(self):
        """Ensure type check is properly called."""
        with pytest.raises(TypeError):
            MathOperation.round('string')
