from tables.units import GroundUnitType, GroundUnitSize

class GroundUnit():
    def __init__(self,):
        self.size = GroundUnitSize.DIVISION
        self.type = GroundUnitType.INFANTRY
        self.type_additional = None
        self.name = '98'
        self.movement = 14
        self.attack = 20
        self.defence = 21
        self.anti_aircraft = 0


    def move_stack(self,start, stop):
        pass
    
    def attack_stack(self):
        pass

    def defend_stack(self):
        pass
