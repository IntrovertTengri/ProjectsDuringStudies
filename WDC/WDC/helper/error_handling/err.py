

class SwitchQueryException(Exception):
    """Exception raised for errors in switch query
    Missing one or more statements.
    Both the default value and the other cases must be handled
    """

    def __init__(self, message="Missing one or more statements"):
        self.message = message
        super().__init__(self.message)


class VariableArgumentException(Exception):
    """Exception raised when adding variable arguments
    out of the variables Lat, Long, and AnsiData, at least one must be specified
    """

    def __init__(self, message="Out of the variables Lat, Long, and AnsiData, at least one must be specified."):
        self.message = message
        super().__init__(self.message)


class NetworkRequestError(Exception):
    """Exception raised for network request errors"""

    def __init__(self, message="Network request failed"):
        self.message = message
        super().__init__(self.message)


class InvalidRequestError(Exception):
    """Exception raised for invalid requests"""

    def __init__(self, message="request argument must be one of the following: ['GetCapabilities', 'DescribeCoverage', 'GetCoverage']"):
        self.message = message
        super().__init__(self.message)


class NoQuerySpecifiedException:
    """
    Exception raised when a query is expected but not specified.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self):
        super().__init__("No query is specified for this Datacube object.")


class NoCoverageException(Exception):
    """
    Exception raised when a coverage is expected but not specified.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self):
        super().__init__("No coverage is specified.")
