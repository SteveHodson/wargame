from tables.constants import GroundUnitSize, GroundUnitType
from data.hex import Hex

class GroundUnit():
    def __init__(self,size, type, name, mp, at, df=None, aa=None, type_additional=None):
        self.size = size
        self.type = type
        self.type_additional = type_additional
        self.name = name
        self.movement = mp
        self.attack = at
        self.defence = df
        self.anti_aircraft = aa


    def move_stack(self,start, stop):
        pass
    
    def attack_stack(self):
        pass

    def defend_stack(self):
        pass
    def __repr__(self) -> str:
        return f'{self.name} - {GroundUnitSize(self.size).name} - {GroundUnitType(self.type).name}'

class GroundUnitStack():
    def __init__(self, hex: Hex) -> None:
        self.hex = hex
        self.stack = []
        self.active_stack = []

    def add_unit(self, grnd_unit: GroundUnit):
        self.stack.append(grnd_unit)

    def make_active(self, grnd_unit: GroundUnit):
        self.active_stack.append(grnd_unit)
        if grnd_unit not in self.stack:
            self.add_unit(grnd_unit)
    
    def display_all(self):
        for s in self.stack:
            print(s)
