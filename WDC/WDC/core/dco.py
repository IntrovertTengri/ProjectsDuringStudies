from .dbc import Dbc
from WDC.helper.error_handling.type_checks import type_check_for_binary_and_numeric_operations
from WDC.helper.error_handling.type_checks import is_string, data_format_exists
from WDC.helper.error_handling.err import VariableArgumentException
from .switch import Switch
from .coverage import Coverage


class Dco:
    """
    Manages the creation and execution of WCPS queries using various components and operations.

    Attributes:
        _dbc (Dbc): The database connection object used to execute queries.
        _coverages (list): A list of Coverage objects over which operations are performed.
        _returnQuery (str): The dynamically constructed WCPS query as a string.

    Methods:
        condenser: Adds a CoverageCondenser operation to the query.
        switch: Adds a Switch operation to the query.
        return_expression: Sets a direct expression to be returned by the query.
        construct: Constructs a customized query using coverages.
        clip: Adds a clipping operation to the query based on provided polygon coordinates.
        execute: Executes the constructed WCPS query using the associated Dbc object.
    """
    _returnQuery = "1"

    def __init__(self, *coverages, dbc: Dbc):
        """
        Initializes the Dco instance with a database connection and one or more coverages.

        Args:
            dbc (Dbc): An instance of the Dbc class for database connection.
            coverages: A variable number of Coverage instances to be managed.

        Raises:
            TypeError: If dbc is not an instance of Dbc or if any of coverages are not Coverage instances.
        """
        if not isinstance(dbc, Dbc):
            raise TypeError('A Dbc object must be passed.')

        if not all(isinstance(coverage, Coverage) for coverage in coverages):
            raise TypeError(
                'All coverages must be instances of the Coverage class.')

        self._dbc = dbc
        self._coverages = list(coverages)

    def switch(self, *cases, default):
        """ Sets up on the fly switch querying

        Args:
            default (RGB): RGB class instance that is set as the default value of the switch
            cases (Case): Variable number of Case objects to set as cases of the switch.

        Returns:
            the instance itself to be used in method chaining
        """
        switch = Switch(*cases, default=default)
        self._returnQuery = f'{switch}'
        return self

    def return_expression(self, expression):
        """
        Sets a direct expression to be used in the query return statement.

        Args:
            expression (str): The expression to be returned by the query.

        Raises:
            TypeError: If the expression is not suitable for binary or numeric operations.
        """
        type_check_for_binary_and_numeric_operations(expression)
        self._returnQuery = f'''{expression}'''
        return self

    def construct(self, values: list[tuple], operator: str):
        """
        Constructs a coverage query using the specified operator and value ranges.

        Args:
            values (list[tuple]): A list of tuples representing the coverage ranges.
            operator (str): The arithmetic operator to apply between coverages.

        Raises:
            VariableArgumentException: If the input values do not meet the expected format or types.

        Returns:
            Dco: Returns self to allow method chaining.
        """
        if len(values) != 2:
            raise VariableArgumentException(
                'Argument must consist of a list of 2 tuples.')
        coverages = []
        for value in values:
            if len(value) != 2 or any(not isinstance(el, (int, float)) for el in value):
                raise VariableArgumentException('Tuple values are incorrect.')
            coverages.append(f"({value[0]}:{value[1]})")
        self._returnQuery = f"coverage myCoverage\nover $p x({coverages[0]}), $q y({coverages[1]}) values $p {operator} $q"
        return self

    def clip(self, values: list[tuple]):
        """
        Constructs a clipping operation for the query based on polygon coordinates.

        Args:
            values (list[tuple]): A list of tuples representing polygon vertices.

        Raises:
            VariableArgumentException: If the input values do not meet the expected format or types.

        Returns:
            Dco: Returns self to allow method chaining.
        """
        polygon = []
        for value in values:
            if len(value) != 2 or any(not isinstance(el, (int, float)) for el in value):
                raise VariableArgumentException('Tuple values are incorrect.')
            polygon.append(f"{value[0]} {value[1]}")
        polygon = f"POLYGON(({','.join(polygon)}))"
        self._returnQuery = f"clip({self._coverages[0].variable}, {polygon})"
        return self

    def execute(self, return_format: str = None):
        """
        Executes the constructed query and returns the response.

        Args:
            return_format (str, optional): Specifies the format in which to return the query result.

        Returns:
            Response: The result of the executed query, formatted according to return_format if specified.
        """
        if return_format is not None:
            is_string(return_format)
            data_format_exists(return_format)

        for_query = 'for '
        if len(self._coverages) > 1:
            for_query += ',\n'.join(
                f"{coverage.get_variable_name()} in ({coverage.get_used_coverage()})" for coverage in self._coverages[:-1])
            for_query += f"\n{self._coverages[-1].get_variable_name()} in ({self._coverages[-1].get_used_coverage()})"
        else:
            coverage = self._coverages[0]
            for_query += f"{coverage.get_variable_name()} in ({coverage.get_used_coverage()})"

        if return_format:
            self._returnQuery = f'encode({self._returnQuery}, "{return_format}")'
        query = f"{for_query} return {self._returnQuery}"
        return self._dbc.post_query(query)
