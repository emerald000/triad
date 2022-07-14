from enum import IntEnum


class Location(IntEnum):
    TOP_LEFT = 0
    TOP = 1
    TOP_RIGHT = 2
    LEFT = 3
    MIDDLE = 4
    RIGHT = 5
    BOTTOM_LEFT = 6
    BOTTOM = 7
    BOTTOM_RIGHT = 8

    def get_adjacent_top(self):
        if self < 2:
            return None
        else:
            return self - 3

    def get_adjacent_right(self):
        if self % 3 == 2:
            return None
        else:
            return self + 1

    def get_adjacent_bottom(self):
        if self > 5:
            return None
        else:
            return self + 3

    def get_adjacent_left(self):
        if self % 3 == 0:
            return None
        else:
            return self - 1
