#!/usr/bin/python3
"""A module that defines a square """

class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represents the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        self._size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return self.size * self.size
