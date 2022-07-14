from typing import List, Dict, Tuple

from Card import Card
from DeckCard import DeckCard
from Faction import Faction
from Rules import Rules


class Position:
    own_deck: List[DeckCard] = None
    opponent_deck: List[DeckCard] = None
    board: List[List[Tuple[Card, bool] | None]] = None
    rules: Rules = None
    human_to_play: bool = None
    boosts: Dict[Faction, int] = None

    def __init__(self):
        self.reset()

    def reset(self):
        self.own_deck = []
        self.opponent_deck = []
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.rules = Rules(0)
        self.human_to_play = False
        self.boosts = {Faction.NONE: 0,
                       Faction.BEASTMAN: 0,
                       Faction.GARLEAN: 0,
                       Faction.PRIMAL: 0,
                       Faction.SCIONS: 0}
