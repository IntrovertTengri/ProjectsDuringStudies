# here you can find functional tests, where Coverage and AxisSubset classes are combined

import pytest
from WDC.core.coverage import Coverage, AxisSubset
from WDC.helper.util.useful_classes import Date


class TestCoverage:
    def test_coverage_initialization_valid(self):
        """Test that the Coverage initializes correctly with valid parameters."""
        coverage = Coverage('CoverageName')
        assert coverage.get_used_coverage() == 'CoverageName'

    def test_coverage_intialization_list_of_coverages(self):
        """Tests that the Coverage accepts multiple arguments as coverage names and combines them into a single string."""
        coverage = Coverage(
            ["CoverageName1", "CoverageName2", "CoverageName3"])
        assert coverage.get_used_coverage() == "CoverageName1, CoverageName2, CoverageName3"


class TestAxis:
    def test_axis_initialization_valid(self):
        """Test that the Axis initializes correctly with valid parameters."""
        axis = AxisSubset("time", (Date(2020), Date(2021)))
        assert axis.axis_name == "time"
        assert str(axis.axis_range[0]) == '"2020"'
        assert str(axis.axis_range[1]) == '"2021"'
        assert axis.get_axis_with_interval() == 'time("2020":"2021")'

    def test_axis_initialization_without_boundaries_raises_error(self):
        """Test that an Axis without boundaries raises a ValueError."""
        with pytest.raises(TypeError):
            AxisSubset("latitude")

    def test_axis_initialization_with_incorrect_range(self):
        """Test that an Axis with invalid range raises a ValueError."""
        with pytest.raises(ValueError):
            AxisSubset("latitude", (1, 2, 3))

    def test_axis_initialization_with_incorrect_type(self):
        """Test that an Axis with invalid range type raises a TypeError."""
        with pytest.raises(TypeError):
            AxisSubset("latitude", "string type")


@pytest.fixture
def coverage():
    return Coverage("CoverageName")


def axis1():
    return AxisSubset("time", (Date(2020), Date(2021)))


def axis2():
    return AxisSubset("latitude", (0, 90))


class TestSetSubset:
    def test_set_subset_valid(self, coverage):
        """Test setting a valid subset."""
        ax1 = axis1()
        ax2 = axis2()
        coverage.set_subset(ax1, ax2)
        expected_subset = '[time("2020":"2021"), latitude(0:90)]'
        assert coverage.subset == expected_subset

    def test_set_subset_with_invalid_axis_raises_error(self, coverage):
        """Test setting a subset with an invalid axis type raises TypeError."""
        invalid_axis = "NotAnAxisInstance"
        with pytest.raises(TypeError):
            coverage.set_subset(invalid_axis)

    def test_set_subset_with_no_axes_raises_error(self, coverage):
        """Test setting a subset with no axes raises an appropriate error."""
        with pytest.raises(ValueError):
            coverage.set_subset()
