"""File to define Bear class"""


__author__ = "730572335"


class Bear:
    """Makes a type Bear class."""
    age: int
    hunger_score: int

    def __init__(self):
        """Contructs the age and hunger score of the bear."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Changes the age and hunger score by day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Changes the hunger score of bears depending on the number of fish."""
        for i in range(num_fish):
            self.hunger_score += 1