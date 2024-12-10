from WDC.helper.error_handling.type_checks import type_check_for_binary_and_numeric_operations


class OperatorOverloading:
    """
    Base class implementing operator overloading for arithmetic and comparison operations.

    Overloads the various operators such as +, -, <,> in its various methods

    Returns for each method either:
        BinaryArithmeticOperation(for arithmetic operations) or BinaryComparisonOperation(for comparison opeartions)

    """

    def __add__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryArithmeticOperation(self, '+', other)

    def __sub__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryArithmeticOperation(self, '-', other)

    def __mul__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryArithmeticOperation(self, '*', other)

    def __truediv__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryArithmeticOperation(self, '/', other)

    def __lt__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '<', other)

    def __le__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '<=', other)

    def __eq__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '=', other)

    def __ne__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '!=', other)

    def __gt__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '>', other)

    def __ge__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '>=', other)


class BinaryArithmeticOperation:
    """
    Class representing binary arithmetic operations between expressions.

    Implements methods of the basic arithmetic operators such as +,-,*,/

    Returns for each method:
         an instance of itself(BinaryArithmeticOperation): The string form of the arithmetic operation.
    """

    def __init__(self, left, operator, right):
        """
        Initialize a binary arithmetic operation with left and right expressions and an operator.

        Parameters:
            left: The left expression.
            operator (str): The binary arithmetic operator.
            right: The right expression.
        """
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"({self.left} {self.operator} {self.right})"

    def __add__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryArithmeticOperation(self, '+', other)

    def __sub__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryArithmeticOperation(self, '-', other)

    def __mul__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryArithmeticOperation(self, '*', other)

    def __truediv__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryArithmeticOperation(self, '/', other)


class BinaryComparisonOperation:
    """
    Class representing binary comparison operations between expressions.

    Implements methods of the basic comaprison operators such as <,>,==,!=,<=,>=,and,or,xor

    Returns for each method:
         an instance of itself(BinaryComparisonOperation): The string form of the comparison operation.
    """

    def __init__(self, left, operator, right):
        """
        Initialize a binary comparison operation with left and right expressions and an operator.

        Parameters:
            left: The left expression.
            operator (str): The binary comparison operator.
            right: The right expression.
        """
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"({self.left} {self.operator} {self.right})"

    def __lt__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '<', other)

    def __le__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '<=', other)

    def __eq__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '=', other)

    def __ne__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '!=', other)

    def __gt__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '>', other)

    def __ge__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, '>=', other)

    def __and__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, 'and', other)

    def __or__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, 'or', other)

    def __xor__(self, other):
        type_check_for_binary_and_numeric_operations(other)
        return BinaryComparisonOperation(self, 'xor', other)
