class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initializes a Square instance with size."""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the Square instance."""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
