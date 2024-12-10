class Date:
    """
    A class representing a date with optional year, month, and day components.

    Attributes:
        year (int): The year component of the date.
        month (int, optional): The month component of the date. Defaults to None.
        day (int, optional): The day component of the date. Defaults to None.

    Methods:
        get_year(): Returns the year component.
        get_month(): Returns the month component if it is not None.
        get_day(): Returns the day component if it is not None.
        set_year(year): Sets the year component.
        set_month(month): Sets the month component.
        set_day(day): Sets the day component.
    """

    def __init__(self, year, month=None, day=None):
        """
        Initializes a Date object with optional month and day values.
        Validates that the year has exactly four digits.
        Month and day, if provided as single digits, are formatted with leading zeros.
        Arguments:
        - year: int, the year component of the date.
        - month: int, optional, the month component of the date. Defaults to None.
        - day: int, optional, the day component of the date. Defaults to None.

        Raises:
        - ValueError: If the year does not have exactly four digits.
        """
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)

    def get_year(self):
        """Returns the year component as a formatted string."""
        return f'"{self.year}"'

    def get_month(self):
        """Returns the month component as a formatted string if it is not None."""
        if self.month is not None:
            return f'"{self.month}"'

    def get_day(self):
        """Returns the day component as a formatted string if it is not None."""
        if self.day is not None:
            return f'"{self.day}"'

    def set_year(self, year):
        """
        Updates the year component of the date.
        Validates that the year has exactly four digits.
        Raises:
        - ValueError: If the year does not have exactly four digits.
        """
        if not isinstance(year, int) or len(str(year)) != 4:
            raise ValueError("Year must be a four-digit integer.")
        self.year = year

    def set_month(self, month):
        """
        Updates the month component of the date.
        Formats the month with a leading zero if it is a single digit.
        """
        if month is not None and (month < 1 or month > 12):
            raise ValueError("Month must be between 1 and 12.")
        self.month = f"{month:02}" if month is not None else None

    def set_day(self, day):
        """
        Updates the day component of the date.
        Formats the day with a leading zero if it is a single digit.
        """
        if day is not None and (day < 1 or day > 31):
            raise ValueError("Day must be between 1 and 31.")
        self.day = f"{day:02}" if day is not None else None

    def __repr__(self):
        """
        Returns a formal string representation of the Date object.
        The format changes based on whether month or day are None.
        """
        if self.month is None and self.day is None:
            return f'"{self.year}"'
        elif self.month is None:
            return f'"{self.year}"'
        elif self.day is None:
            return f'"{self.year}-{self.month}"'
        else:
            return f'"{self.year}-{self.month}-{self.day}"'

    def __str__(self):
        """
        Returns a readable string representation of the Date object.
        Similar to __repr__, the output adjusts based on set attributes.
        """
        if self.month is None and self.day is None:
            return f'"{self.year}"'
        elif self.month is None:
            return f'"{self.year}"'
        elif self.day is None:
            return f'"{self.year}-{self.month}"'
        else:
            return f'"{self.year}-{self.month}-{self.day}"'


class RGB:
    """
    A class representing RGB color model with red, green, and blue components.

    Attributes:
        red (int): Value for the red component (0-255).
        green (int): Value for the green component (0-255).
        blue (int): Value for the blue component (0-255).

    Methods:
        get_red(): Returns the red component.
        get_green(): Returns the green component.
        get_blue(): Returns the blue component.
        set_red(red): Sets the red component.
        set_green(green): Sets the green component.
        set_blue(blue): Sets the blue component.
    """

    def __init__(self, red, green, blue):
        """
        Initializes an RGB color object.
        Arguments:
        - red: int, value for the red component (0-255).
        - green: int, value for the green component (0-255).
        - blue: int, value for the blue component (0-255).

        Raises:
        - ValueError: If any of the components are not integers or are outside the 0-255 range.
        """
        self.set_red(red)
        self.set_green(green)
        self.set_blue(blue)

    def get_red(self):
        """Returns the value of the red component."""
        return self.red

    def get_green(self):
        """Returns the value of the green component."""
        return self.green

    def get_blue(self):
        """Returns the value of the blue component."""
        return self.blue

    def set_red(self, red):
        """
        Updates the red component of the color.
        Raises:
        - ValueError: If the value is not an integer or is outside the 0-255 range.
        """
        if not isinstance(red, int) or not 0 <= red <= 255:
            raise ValueError("Red value must be an integer between 0 and 255.")
        self.red = red

    def set_green(self, green):
        """
        Updates the green component of the color.
        Raises:
        - ValueError: If the value is not an integer or is outside the 0-255 range.
        """
        if not isinstance(green, int) or not 0 <= green <= 255:
            raise ValueError(
                "Green value must be an integer between 0 and 255.")
        self.green = green

    def set_blue(self, blue):
        """
        Updates the blue component of the color.
        Raises:
        - ValueError: If the value is not an integer or is outside the 0-255 range.
        """
        if not isinstance(blue, int) or not 0 <= blue <= 255:
            raise ValueError(
                "Blue value must be an integer between 0 and 255.")
        self.blue = blue

    def __repr__(self):
        """
        Returns a formal string representation of the RGB object, showing all color components.
        """
        return '{' + f'red: {self.red}; green: {self.green}; blue: {self.blue}' + '}'

    def __str__(self):
        """
        Returns a readable string representation of the RGB object, showing all color components.
        Similar to __repr__.
        """
        return '{' + f'red: {self.red}; green: {self.green}; blue: {self.blue}' + '}'
