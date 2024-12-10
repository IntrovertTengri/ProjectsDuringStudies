import pytest
from unittest.mock import patch
from WDC.helper.operations.numoperations import AggregationMethod
from WDC.core.coverage import Coverage

@pytest.fixture
def setUpCoverage():
    return Coverage("CoverageName")

class TestAggregate:
    """Unit tests for AggregateMethod class."""

    def test_intialization(self, setUpCoverage):
        """Testing initialization of the AggregationMethod instance, when different parameters passed."""
        my_agg = AggregationMethod('min', setUpCoverage)
        assert str(my_agg.expression) == str(setUpCoverage)
        assert my_agg.operation == 'min'
        assert str(my_agg) == f'min({setUpCoverage.get_variable_name()})' 

    @pytest.mark.parametrize("method, operation", [
        ('min', 'min'),
        ('max', 'max'),
        ('avg', 'avg'),
        ('count', 'count'),
        ('sum', 'sum')
    ])

    def test_operations(self, method, operation, setUpCoverage):
        """Testing usage of different aggregation methods"""
        with patch('WDC.helper.error_handling.type_checks.type_check_for_binary_and_numeric_operations'):
            operation_class = getattr(AggregationMethod, method)
            result = operation_class(setUpCoverage)
            assert isinstance(result, AggregationMethod)
            assert str(result.operation) == operation
            assert str(result.expression) == str(setUpCoverage)
            assert str(result) == str(f'{method}({setUpCoverage})')

    def test_incorrect_type_check(self):
        """Ensure type check is properly called."""
        with pytest.raises(TypeError):
            AggregationMethod.min('string')
        with pytest.raises(TypeError):
            AggregationMethod.max('string')
        with pytest.raises(TypeError):
            AggregationMethod.avg('string')
        with pytest.raises(TypeError):
            AggregationMethod.sum('string')
        with pytest.raises(TypeError):
            AggregationMethod.count('string')

