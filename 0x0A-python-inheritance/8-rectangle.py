#!/usr/bin/python3
class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the Rectangle instance."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
