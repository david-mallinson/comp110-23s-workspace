"""File to define River class."""


__author__ = "730572335"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Makes a type River class."""
    day: int = 0
    bears: list[Bear]
    fish: list[Fish]
    

    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the age of each animal and if they should be removed from the list."""
        fish_pop = []
        for f in self.fish:
            if f.age > 3:
                continue
            fish.pop.append(f)
        self.fish = fish.pop

        bear_pop = []
        for b in self.bears:
            if b.age > 5:
                continue
            bear_pop.append(b)
        self.bears = bear_pop

        return None

    def bears_eating(self):
        """Sees how many fish the bears will eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks the hunger score."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                continue
            new_bears.append(bear)
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """Reproducing the amount of fish."""
        populated_fish: list[Fish] = []
        for x in range((len(self.fish) // 2) * 4):
            populated_fish.append(x)
        self.fish += populated_fish
        return None
    
    def repopulate_bears(self):
        """Reproducing the amount of bears."""
        populated_bear: list[Bear] = []
        for x in range(len(self.bears) // 2):
            populated_bear.append(x)
        self.bears += populated_bear
        return None
    
    def view_river(self):
        """Shows the population and day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"BEar population: {len(self.bears)}")
        return None
    
    def one_river_week(self):
        """Simulates one week of life of the river."""
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1

    def remove_fish(self, amount: int) -> None:
        """Removes whatever inputed amount of fish."""
        for _ in range(amount):
            self.fish.pop(0)

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()