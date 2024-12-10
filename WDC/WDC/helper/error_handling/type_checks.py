from WDC.helper.util.constants import dictionary_of_data_formats


def is_string(variable):
    """
    Checks if the variable is a string.

    Args:
        variable (any): Variable to check.

    Returns:
        bool: True if the variable is a string, otherwise raises TypeError.

    Raises:
        TypeError: If the variable is not a string.
    """
    if not isinstance(variable, str):
        raise TypeError("The value passed must be a string")
    return True


def is_list_of_strings(lst):
    """
    Checks if the list contains only strings.

    Args:
        lst (list): List to check.

    Returns:
        bool: True if the list contains only strings, otherwise raises TypeError.

    Raises:
        TypeError: If the list does not contain only strings.
    """
    if not isinstance(lst, list):
        raise TypeError("The value passed must be a list of strings.")
    for item in lst:
        is_string(item)
    return True


def type_check_subset(argument, additional_type):
    """
    Checks if the argument is of type int, float, str, or a specified additional type.

    Args:
        argument (any): Argument to check.
        additional_type (type): Additional type that the argument could be.

    Raises:
        TypeError: If the argument is not of the correct type.
    """
    if not isinstance(argument, (str, int, float, additional_type)):
        raise TypeError(
            f"The arguments must be int, float, or {additional_type}")


def type_check_for_binary_and_numeric_operations(instance_to_check):
    """
    Validates the type of the instance to ensure it is appropriate for binary and numeric operations.

    This function checks if the instance belongs to a set of allowed types suitable for various
    operations like arithmetic or comparison within a system. If the instance is not one of the
    allowed types, the function raises a TypeError.

    Args:
        instance_to_check (any): The instance whose type is to be validated.

    Raises:
        TypeError: If the type of `instance_to_check` is not one of the permitted types.

    Allowed Types:
        - 'Coverage': Represents a data coverage object.
        - 'BinaryArithmeticOperation': Represents an arithmetic operation involving two operands.
        - 'BinaryComparisonOperation': Represents a comparison operation involving two operands.
        - 'int': The integer data type.
        - 'float': The floating-point data type.
        - 'AggregationMethod': Represents a method for data aggregation.
        - 'MathOperation': Represents a mathematical operation.
    """
    allowed_types = {
        'Coverage',
        'BinaryArithmeticOperation',
        'BinaryComparisonOperation',
        'int',
        'float',
        'AggregationMethod',
        'MathOperation'
    }
    if type(instance_to_check).__name__ not in allowed_types:
        raise TypeError("The type of the instance you passed is not allowed.")


def data_format_exists(data_format: str):
    """
    Checks if a given data format exists in the dictionary of data formats and returns its MIME type.

    Args:
        data_format (str): The data format to check in the dictionary.

    Returns:
        str: The MIME type associated with the given data format.

    Raises:
        KeyError: If the data format does not exist in the dictionary.
    """
    try:
        return dictionary_of_data_formats[data_format]
    except:
        raise KeyError("Such data format does not exist.")
