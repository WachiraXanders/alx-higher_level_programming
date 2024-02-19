#!/usr/bin/python3
class MyList(list):
    """A custom list class that inherits from list."""

    def print_sorted(self):
        """Prints the list in sorted order (ascending)."""
        sorted_list = sorted(self)
        print(sorted_list)
