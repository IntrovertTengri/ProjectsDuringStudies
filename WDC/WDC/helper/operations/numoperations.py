from .binary_expressions import OperatorOverloading
from WDC.helper.error_handling.type_checks import type_check_for_binary_and_numeric_operations


class AggregationMethod(OperatorOverloading):
    """
    A class to represent aggregation operations in WCPS queries.
    It supports max, min, avg, sum, and count operations.

    Attributes:
        operation (str): The name of the operation (e.g., 'max', 'min').
        expression (str): The expression over which the operation is performed.

    Methods:
        max, min, avg, sum, count: Class methods to instantiate the class
        with specific operations.
    """
    def __init__(self, operation, expression):
        """
        Initialize an AggregationMethod instance.

        Args:
            operation (str): The aggregation operation (e.g., 'max', 'min').
            expression (str): The expression to apply the operation to.
        """
        self.operation = operation
        self.expression = expression

    def __str__(self):
        """
        String representation of the AggregationMethod instance.

        Returns:
            str: A string that represents the object in the format operation(expression).
        """
        return f'{self.operation}({self.expression})'

    def __repr__(self):
        """
        Official string representation of the AggregationMethod instance.

        Returns:
            str: The string representation of the object.
        """
        return self.__str__()

    @classmethod
    def max(cls, expression):
        """
        Create an instance to calculate the maximum value of an expression.

        Args:
            expression (str): The expression to calculate the maximum for.

        Returns:
            AggregationMethod: Instance configured to perform the 'max' operation.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='max', expression=expression)

    @classmethod
    def min(cls, expression):
        """
        Create an instance to calculate the minimum value of an expression.

        Args:
            expression (str): The expression to calculate the minimum for.

        Returns:
            AggregationMethod: Instance configured to perform the 'min' operation.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='min', expression=expression)

    @classmethod
    def avg(cls, expression):
        """
        Create an instance to calculate the average value of an expression.

        Args:
            expression (str): The expression to calculate the average for.

        Returns:
            AggregationMethod: Instance configured to perform the 'avg' operation.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='avg', expression=expression)

    @classmethod
    def sum(cls, expression):
        """
        Create an instance to calculate the sum of values of an expression.

        Args:
            expression (str): The expression to calculate the sum for.

        Returns:
            AggregationMethod: Instance configured to perform the 'sum' operation.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='sum', expression=expression)

    @classmethod
    def count(cls, expression):
        """
        Create an instance to count the occurrences within an expression.

        Args:
            expression (str): The expression to count occurrences in.

        Returns:
            AggregationMethod: Instance configured to perform the 'count' operation.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='count', expression=expression)

    

class MathOperation(OperatorOverloading):
    """
    Represents arithmetic operations for expressions, supporting basic and advanced mathematical functions.

    Attributes:
        operation (str): The name of the mathematical operation.
        expression (str): The expression to which the operation is applied, could be a single value or a comma-separated pair of values.

    Methods:
        __str__: Returns a string representation of the mathematical operation.
        round: Rounds the value of an expression.
        abs: Returns the absolute value of an expression.
        mod: Calculates the modulus of two expressions.
        floor: Rounds down the value of an expression.
        ceil: Rounds up the value of an expression.
        exp: Calculates the exponential of an expression.
        ln: Calculates the natural logarithm of an expression.
        sqrt: Calculates the square root of an expression.
        log: Calculates the logarithm of an expression to a specified base.
        pow: Raises a base to a specified exponent.
        sin: Calculates the sine of an expression.
        cos: Calculates the cosine of an expression.
        tan: Calculates the tangent of an expression.
        sinh: Calculates the hyperbolic sine of an expression.
        cosh: Calculates the hyperbolic cosine of an expression.
        tanh: Calculates the hyperbolic tangent of an expression.
        arcsin: Calculates the inverse sine of an expression.
        arccos: Calculates the inverse cosine of an expression.
        arctan: Calculates the inverse tangent of an expression.
        atan2: Calculates the inverse tangent of two expressions.
    """

    def __init__(self, operation, expression):
        """
        Initializes a MathOperation object with specified operation and expression.

        Args:
            operation (str): The mathematical operation to perform.
            expression (str): The expression on which to perform the operation.
        """
        self.operation = operation
        self.expression = expression

    def __str__(self):
        """Returns the string representation of the MathOperation."""
        return f'''{self.operation}({self.expression})'''

    @classmethod
    def round(cls, expression):
        """
        Class method to round the value of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='round', expression=expression)

    @classmethod
    def abs(cls, expression):
        """
        Class method to perform absolute value on an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='abs', expression=expression)

    @classmethod
    def mod(cls, dividend, divisor):
        """
        Class method to perform modulus operation.
        """
        type_check_for_binary_and_numeric_operations(dividend)
        type_check_for_binary_and_numeric_operations(divisor)
        return cls(operation='mod', expression=f'''{dividend}, {divisor}''')

    @classmethod
    def floor(cls, expression):
        """
        Class method to round down the value of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='floor', expression=expression)

    @classmethod
    def ceil(cls, expression):
        """
        Class method to round up the value of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='ceil', expression=expression)

    @classmethod
    def exp(cls, expression):
        """
        Class method to calculate the exponential value of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='exp', expression=expression)

    @classmethod
    def ln(cls, expression):
        """
        Class method to calculate the natural logarithm of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='ln', expression=expression)

    @classmethod
    def sqrt(cls, expression):
        """
        Class method to calculate the square root of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='sqrt', expression=expression)

    @classmethod
    def log(cls, antilogarithm, base):
        """
        Class method to calculate the logarithm of an expression to a specified base.
        """
        type_check_for_binary_and_numeric_operations(antilogarithm)
        type_check_for_binary_and_numeric_operations(base)
        return cls(operation='log', expression=f'''{antilogarithm}, {base}''')

    @classmethod
    def pow(cls, base, exponent):
        """
        Class method to raise a base expression to a specified exponent.
        """
        type_check_for_binary_and_numeric_operations(base)
        type_check_for_binary_and_numeric_operations(exponent)
        return cls(operation='pow', expression=f'''{base}, {exponent}''')

    @classmethod
    def sin(cls, expression):
        """
        Class method to calculate the sine of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='sin', expression=expression)

    @classmethod
    def cos(cls, expression):
        """
        Class method to calculate the cosine of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='cos', expression=expression)

    @classmethod
    def tan(cls, expression):
        """
        Class method to calculate the tangent of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='tan', expression=expression)

    @classmethod
    def sinh(cls, expression):
        """
        Class method to calculate the hyperbolic sine of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='sinh', expression=expression)

    @classmethod
    def cosh(cls, expression):
        """
        Class method to calculate the hyperbolic cosine of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='cosh', expression=expression)

    @classmethod
    def tanh(cls, expression):
        """
        Class method to calculate the hyperbolic tangent of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='tanh', expression=expression)

    @classmethod
    def arcsin(cls, expression):
        """
        Class method to calculate the inverse sine (arcsine) of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='arcsin', expression=expression)

    @classmethod
    def arccos(cls, expression):
        """
        Class method to calculate the inverse cosine (arccosine) of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='arccos', expression=expression)

    @classmethod
    def arctan(cls, expression):
        """
        Class method to calculate the inverse tangent (arctangent) of an expression.
        """
        type_check_for_binary_and_numeric_operations(expression)
        return cls(operation='arctan', expression=expression)

    @classmethod
    def atan2(cls, x, y):
        """
        Class method to calculate the inverse tangent of the quotient of two numbers.
        """
        type_check_for_binary_and_numeric_operations(x)
        type_check_for_binary_and_numeric_operations(y)
        return cls(operation='atan2', expression=f'''{x}, {y}''')
