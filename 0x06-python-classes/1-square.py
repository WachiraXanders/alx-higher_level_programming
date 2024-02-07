#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square."""
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        """Initialize a square with an optional name.

        Args:
            new_name (str, optional): The name for the square.
        """
        self.is_new = True
        if new_name is not None:
            self.name = new_name


if __name__ == "__main__":
    # Example usage
    u = Square("John")
    print(u.name)
