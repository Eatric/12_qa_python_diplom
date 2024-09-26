from praktikum.engine import Engine
from praktikum.frame import Frame


class Car:

    def __init__(self, name):
        self.engine = None
        self.frame = None
        self.name = name

    def set_engine(self, engine: Engine):
        self.engine = engine

    def set_frame(self, frame: Frame):
        self.frame = frame

    def get_weight(self):
        return (self.frame.get_weight() + self.engine.get_weight()) * 2