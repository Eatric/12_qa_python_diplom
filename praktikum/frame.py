from praktikum.colors import Color


class Frame:

    def __init__(self, name, color: Color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def get_color(self) -> Color:
        return self.color

    def get_weight(self) -> int:
        return self.weight