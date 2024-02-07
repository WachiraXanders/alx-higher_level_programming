#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int or float, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square is less than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square is less than the other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square is less than or equal to the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square is less than or equal to the other, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square is greater than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square is greater than the other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square is greater than or equal to the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if this square is greater than or equal to the other, False otherwise.
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    # Example usage
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
