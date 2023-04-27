"""File to define Fish class"""


__author__ = "730572335"


class Fish:
    """Makes a type fish class."""
    age: int = 0

    def __init__(self):
        """Constructs the age."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increase the age by the day."""
        self.age += 1
        return None