#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size


if __name__ == "__main__":
    # Example usage
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
