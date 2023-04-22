from enum import Enum
from terrain import Terrain

class GroundUnitStack():
    def __init__(self):
        self.units = [Ground_Unit()]
        self.terrain = Terrain()

    def move_stack(self,start, stop):
        pass
    
    def attack_stack(self):
        pass

    def defend_stack(self):
        pass


class Ground_Unit():
    def __init__(self):
        self.size = GroundUnitSize.DIVISION
        self.type = GroundUnitType.INFANTRY
        self.type_additional = None
        self.name = '98'
        self.movement = 14
        self.attack = 20
        self.defence = 21
        self.anti_aircraft = 0

class GroundUnitSize(Enum):
    BATTALION = 1
    REGIMENT  = 2
    BRIGADE   = 3
    DIVISION  = 4
    CORPS     = 5

class GroundUnitType(Enum):
    ARMOUR=1
    LIGHT_ARMOUR=2
    MECHANISED=3
    FLAMETHROWER_TANKS=4
    ASSAULT_GUNS=5
    TANK_DESTROYER=6
    ENGINEERING_TANKS=7
    MOTORCYCLE=8
    TRANSPORT=9
    STATIC=10
    QUARTER_MASTER=11
    AIR_QUARTER_MASTER=12
    RIVER_QUARTER_MASTER=13
    SUPPLY_TERMINAL=14
    AIR_GROUP_HQ=15
    INFANTRY=16
    CAVALRY=17
    NAVAL_INFANTRY=18
    BICYCLE_INFANTRY=19
    LIGHT_INFANTRY=20
    FORTRESS=21
    MACHINE_GUN=22
    POLITICAL_POLICE=23
    SECURITY=24
    BORDER=25
    AIRBOURNE=26
    AIR_LANDING=27
    GLIDER=28
    COMMANDO=29
    TRAINING=30
    COMBAT_ENGINEER=31
    CONSTRUCTION_ENGINEER=32
    RAILWAY_ENGINEER=33
    ASSAULT_ENGINEER=34
    BEACH_ENGINEER=35
    PORT_ENGINEER=36
    ARTILLERY=37
    MORTAR=38
    ROCKET_ARTILLERY=39
    SIEGE_ARTILLERY=40
    RAILWAY_SIEGE_ARTILLERY=41
    COASTAL_DEFENSE=42
    ANTI_TANK=43
    LIGHT_ANTI_AIRCRAFT=44
    RESERVE=45

class GroundUnitTypeAdditional(Enum):
    MOTORISED=1
    AIR_DROPPABLE=2
    SKI=3
    RAILWAY=4
    MOUNTAIN=5
    SEMI_MOTORISED=6
    AMPHIBIOUS=7
    HEAVY=8
