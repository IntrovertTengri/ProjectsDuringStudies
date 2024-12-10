from WDC.helper.error_handling.type_checks import is_string, is_list_of_strings
from WDC.helper.operations.binary_expressions import OperatorOverloading
from WDC.helper.util.utils import concat_coverage_names
from WDC.helper.util.useful_classes import Date


class Coverage(OperatorOverloading):
    """
    A Coverage class representing a dataset or variable coverage in query operations. It holds
    information about subsets and variable names related to data coverage.

    Attributes:
        subset (str): The subset string related to the Coverage instance.
        variable (str): A unique variable name associated with the Coverage instance.
        name (str): The name or names of coverages retrieved from the server.
    """
    variable_count = 0

    def __init__(self, coverage_names):
        """
        Initializes a Coverage instance by setting its name and assigning a unique variable name.

        Args:
            coverage_names (str | list of str): Coverage name or list of coverage names.

        Raises:
            TypeError: If `coverage_names` is neither a string nor a list of strings.
        """
        # error handling.
        # check if the passed coverage_name is a list of coverages consisting of strings or just a string
        try:
            if is_string(coverage_names):
                self.name = coverage_names
        except:
            if is_list_of_strings(coverage_names):
                self.name = concat_coverage_names(coverage_names)

        # assigning a variable name to the Coverage instance
        self.variable_count += 1
        self.variable = '$i' + str(Coverage.variable_count)
        self.subset = None

    def get_variable_name(self):
        """Returns the variable name of the Coverage instance."""
        return self.variable

    def get_used_coverage(self):
        """Returns the name of the used coverage."""
        return self.name

    def set_variable_name(self, variable_name):
        """
        Sets the variable name for the Coverage instance.

        Args:
            variable_name (str): The new variable name to be set.

        Raises:
            TypeError: If `variable_name` is not a string.
        """
        is_string(variable_name)
        self.variable = variable_name

    def set_new_coverage(self, coverage_names):
        """
        Updates the coverage name or names.

        Args:
            coverage_names (str | list of str): New coverage name or list of coverage names.

        Raises:
            TypeError: If `coverage_names` is neither a string nor a list of strings.
        """
        try:
            if is_string(coverage_names):
                self.name = coverage_names
        except:
            if is_list_of_strings(coverage_names):
                self.name = concat_coverage_names(coverage_names)

    def set_subset(self, *axises):
        """
        Set the subset of the coverage based on provided axis subsets.

        Args:
            axises (tuple of AxisSubset): Axis subsets to define the subset of the coverage.

        Raises:
            TypeError: If any of the arguments are not instances of AxisSubset or if no axises are provided
        """
        # Checking if every argument is an instance of the class Axis
        if not (all(isinstance(axis, AxisSubset) for axis in axises)):
            raise TypeError(
                "The arguments must be instances of AxisSubset class")
        if len(axises) == 0:
            raise ValueError("No axises provided.")
        # combining all axises to one subset under []
        subset = '''['''
        for axis in axises[:-1]:
            subset += axis.get_axis_with_interval() + ', '
        subset += axises[-1].get_axis_with_interval() + ''']'''

        self.subset = subset

    def __repr__(self):
        """Returns a formal string representation of the Coverage instance."""
        return f'{self.variable}{self.subset if self.subset is not None else ""}'

    def __str__(self):
        """Returns a string representation of the Coverage instance, similar to __repr__."""
        return self.__repr__()


class AxisSubset:
    """
    Class representing an axis in coverage data with optional start and stop boundaries.

    Attributes:
        axis_name (str): Name of the axis.
        start (Date): Optional starting boundary of the axis.
        stop (Date): Optional ending boundary of the axis.
    """

    def __init__(self, axis_name: str, axis_range: tuple):
        """
        Initializes an AxisSubset instance.

        Args:
            axis_name (str): The name of the axis.
            axis_range (Data): contains tuple specifying the range of the axis.

        Raises:
            ValueError: If neither `start` nor `stop` is provided.
        """
        self.set_name(axis_name)
        if axis_range == None:
            raise ValueError("Specify either start or stop range.")
        self.set_range(axis_range)

    def set_name(self, axis_name: str):
        """
        Sets the name of the axis.

        Args:
            axis_name (str): The new name of the axis.

        Raises:
            TypeError: If `axis_name` is not a string.
        """
        is_string(axis_name)
        self.axis_name = axis_name

    def set_range(self, axis_range):
        """
        Sets the range of the axis.

        Args:
            axis_range (tuple): The range of the axis.

        Raises:
            TypeError: If `axis_range` is not a tuple or is more than 2 elements.
        """
        if not isinstance(axis_range, (tuple, int, float, Date)):
            raise TypeError(
                "Incorrect range type.")
        if isinstance(axis_range, tuple) and (len(axis_range) != 2):
            raise ValueError(
                "The range must be a tuple of no more than 2 elements.")
        self.axis_range = axis_range

    def get_axis_with_interval(self):
        """
        Constructs and returns a string representing the axis with its set boundaries.

        Returns:
            str: The string representation of the axis with its interval.
        """
        if type(self.axis_range) is tuple:
            axis_with_interval = f"{self.axis_name}({self.axis_range[0]}:{self.axis_range[1]})"
        else:
            axis_with_interval = f"{self.axis_name}({self.axis_range})"

        return axis_with_interval
