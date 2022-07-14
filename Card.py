from Faction import Faction


class Card:
    def __init__(self, name: str, up: int, right: int, down: int, left: int, faction: Faction, rarity: int, icon: str):
        self.name = name
        self.up = up
        self.right = right
        self.down = down
        self.left = left
        self.faction = faction
        self.rarity = rarity
        self.icon = icon
