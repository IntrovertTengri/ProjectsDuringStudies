
from WDC.helper.util.useful_classes import RGB
from WDC.helper.error_handling.type_checks import type_check_for_binary_and_numeric_operations
from WDC.helper.operations.binary_expressions import BinaryComparisonOperation


class Case:
    """
    A class representing a case in a switch-case structure, specifically designed to handle
    conditions and return values based on those conditions.

    Attributes:
        condition (BinaryComparisonOperation): The condition under which the case is true.
        return_value (RGB | any): The value to return if the condition is true, typically an RGB
                                  object or a value validated by specific type checks.

    Methods:
        set_condition(condition): Sets the condition for the case.
        set_return_value(return_value): Sets the return value for the case.
    """

    def __init__(self, condition, return_value):
        """
        Initializes the Case object with a condition and a return value.

        Args:
            condition (BinaryComparisonOperation): The condition for this case.
            return_value (RGB | any): The return value when the condition is met.

        Raises:
            TypeError: If the condition is not an instance of BinaryComparisonOperation.
        """
        self.set_condition(condition)
        self.set_return_value(return_value)

    def set_condition(self, condition):
        """
        Sets the condition for the case.

        Args:
            condition (BinaryComparisonOperation): The condition to set.

        Raises:
            TypeError: If the condition is not an instance of BinaryComparisonOperation.
        """
        if not isinstance(condition, BinaryComparisonOperation):
            raise TypeError(
                'Please, provide a comparison related to some coverage as an argument.')
        self.condition = condition

    def set_return_value(self, return_value):
        """
        Sets the return value for the case.

        Args:
            return_value (RGB | any): The return value to set. Must be either an RGB object or meet certain type conditions.

        Raises:
            TypeError: If the return_value is not an instance of RGB or does not meet other type checks.
        """
        if not isinstance(return_value, RGB):
            type_check_for_binary_and_numeric_operations(return_value)
        self.return_value = return_value

    def __repr__(self):
        """Returns a formal string representation of the Case object."""
        return f'case {self.condition} return {self.return_value}'

    def __str__(self):
        """Returns the string representation of the Case object, identical to __repr__."""
        return self.__repr__()


class Switch:
    """
    A class representing a switch structure commonly used in WCPS for managing multiple cases.

    Attributes:
        cases (list of Case): A list of Case objects representing individual cases in the switch.
        default (RGB | int, float, Coverage, BinaryArithmeticOperation, AggregationMethod): The default return value if
            none of the cases match.

    Methods:
        set_cases(*cases): Sets the cases for the switch.
        set_default(default): Sets the default return value for the switch.
    """

    def __init__(self, *cases, default):
        """
        Initializes the Switch object with cases and a default case.

        Args:
            *cases (Case): Variable number of Case objects representing the cases of the switch.
            default (RGB | any): The default return value if no cases are met.

        Raises:
            TypeError: If any of the cases are not instances of the Case class.
        """
        self.set_cases(*cases)
        self.set_default(default)

    def set_cases(self, *cases):
        """
        Sets the cases of the switch.

        Args:
            *cases (Case): Variable number of Case objects to set as cases of the switch.

        Raises:
            TypeError: If any argument is not an instance of Case.
        """
        if not all(isinstance(case, Case) for case in cases):
            raise TypeError(
                "All arguments must be instances of the Case class")

        if not cases:
            raise ValueError("Empty arguments.")

        self.cases = list(cases)

    def set_default(self, default):
        """
        Sets the default return value for the switch.

        Args:
            default (RGB | any): The default return value.

        Raises:
            TypeError: If the default is not an instance of RGB or does not meet other type checks.
        """
        if not isinstance(default, RGB):
            type_check_for_binary_and_numeric_operations(default)
        self.default = default

    def __repr__(self):
        """Returns a formal string representation of the Switch object."""
        switch_representation = 'switch\n'
        for case in self.cases:
            switch_representation += str(case) + '\n'
        switch_representation += f'default return {self.default}\n'
        return switch_representation

    def __str__(self):
        """Returns the string representation of the Switch object, identical to __repr__."""
        return self.__repr__()
