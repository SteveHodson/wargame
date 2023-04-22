import random
from enum import Enum
'''
Determine the results of Ground Combat
'''
class GroundCombatResults():

    def __init__(self, drm: int, odds: str):
        self.drm = drm
        self.odds = odds
        self.results = {
            'AE': ('Eliminated','NE','None'),
            'AH': ('Halved','NE','None'),
            'AQ': ('Quartered','NE','None'),
            'HR': ('Halved','Retreats','Defender'),
            'QR': ('Quartered','Retreats','Defender'),
            'HQ': ('Halved','Quartered','Defender Choice'),
            'DR': ('NE','Retreats','Defender'),
            'QH': ('Quartered','Halved','Defender'),
            'EX': ('Note 1','Note 1','Smaller Force 1'),
            'HX': ('Note 2','Note 2','Smaller Force 2'),
            'DQ': ('NE','Quartered','Defender'),
            'DH': ('NE','Halved','Defender'),
            'DE': ('NE','Eliminated','Defender'),
            'DA': ('NE','NE','None')
        }      

    def calculate_combat_result(self):
        combat_results_code = ['AE','AH','AQ','HR','QR','HQ','DR','QH','EX','HX','DQ','DH','DE','DA']
        combat_odds = ['1:4','1:3','1:2','1:1','2:1','3:1','4:1','5:1','6:1','7:1','8:1','9:1']

        modded_roll = _dice(10) + self.drm
        if modded_roll < -4: modded_roll = -4
        if modded_roll > 15: modded_roll = 15

        combat_odds_index = combat_odds.index(self.odds)
        offset = modded_roll - (3 - combat_odds_index)

        if offset < 0: offset = 0
        return combat_results_code[offset]

    def get_effects(self):
        result = self.calculate_combat_result()
        print(result)
        return self.results.get(result)

class Terrain():
    def __init__(self):
        self.ground_unit_effects = {
            'Clear':        {'drm': 0,  'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.25,1), 'others': (1.0,1)},
            'Steppe':       {'drm': 0,  'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.50,1), 'others': (1.0,1)},
            'Hills':        {'drm': -1, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.25,2), 'others': (1.0,2)},
            'Mountains':    {'drm': -2, 'ASE': 'N', GroundUnitTypeAdditional.MOTORISED: (0.50,4), 'others': (1.0,2)},
            'Woods':        {'drm': -1, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.00,2), 'others': (1.0,2)},
            'Wooded Hills': {'drm': -2, 'ASE': 'H', GroundUnitTypeAdditional.MOTORISED: (1.00,3), 'others': (1.0,3)},
            'Stony Hills':  {'drm': -1, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.00,2), 'others': (1.0,2)},
            'Desert':       {'drm': 0,  'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.50,1), 'others': (1.0,1)},
            'Sandy Desert': {'drm': 0,  'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.25,3), 'others': (1.0,2)},
            'Stony Desert': {'drm': 0,  'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.15,3), 'others': (1.0,2)},
            'Salt Marsh':   {'drm': -5, 'ASE': 'N', GroundUnitTypeAdditional.MOTORISED: (0.10,10),'others': (0.1,6)}
        }

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



def _dice(n):
    random.seed()
    return random.randint(1,n)


if __name__ == "__main__":
    print(GroundCombatResults(-2, '5:1').get_effects())