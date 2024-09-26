class Engine:

    def __init__(self, name, power, weight):
        self.name = name
        self.power = power
        self.weight = weight

    def get_name(self) -> str:
        return self.name

    def get_power(self) -> int:
        return self.power

    def get_weight(self) -> int:
        return self.weight