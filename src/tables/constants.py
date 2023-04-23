from enum import Enum
       

class Nation(Enum):
    GERMANY  =1
    ITALY    =2
    ALLIED   =3

class GroundUnitSize(Enum):
    BATTALION = 1
    REGIMENT  = 2
    BRIGADE   = 3
    DIVISION  = 4
    CORPS     = 5

class GroundUnitType(Enum):
    ARMOUR                  =1
    LIGHT_ARMOUR            =2
    MECHANISED              =3
    FLAMETHROWER_TANKS      =4
    ASSAULT_GUNS            =5
    TANK_DESTROYER          =6
    ENGINEERING_TANKS       =7
    MOTORCYCLE              =8
    TRANSPORT               =9
    STATIC                  =10
    QUARTER_MASTER          =11
    AIR_QUARTER_MASTER      =12
    RIVER_QUARTER_MASTER    =13
    SUPPLY_TERMINAL         =14
    AIR_GROUP_HQ            =15
    INFANTRY                =16
    CAVALRY                 =17
    NAVAL_INFANTRY          =18
    BICYCLE_INFANTRY        =19
    LIGHT_INFANTRY          =20
    FORTRESS                =21
    MACHINE_GUN             =22
    POLITICAL_POLICE        =23
    SECURITY                =24
    BORDER                  =25
    AIRBOURNE               =26
    AIR_LANDING             =27
    GLIDER                  =28
    COMMANDO                =29
    TRAINING                =30
    COMBAT_ENGINEER         =31
    CONSTRUCTION_ENGINEER   =32
    RAILWAY_ENGINEER        =33
    ASSAULT_ENGINEER        =34
    BEACH_ENGINEER          =35
    PORT_ENGINEER           =36
    ARTILLERY               =37
    MORTAR                  =38
    ROCKET_ARTILLERY        =39
    SIEGE_ARTILLERY         =40
    RAILWAY_SIEGE_ARTILLERY =41
    COASTAL_DEFENSE         =42
    ANTI_TANK               =43
    LIGHT_ANTI_AIRCRAFT     =44
    RESERVE                 =45

class GroundUnitTypeAdditional(Enum):
    MOTORISED      =1
    AIR_DROPPABLE  =2
    SKI            =3
    RAILWAY        =4
    MOUNTAIN       =5
    SEMI_MOTORISED =6
    AMPHIBIOUS     =7
    HEAVY          =8
    OTHERS         =9

class CityType(Enum):
    LARGE             =1
    MEDIUM            =2
    SMALL             =3
    POINT_OF_INTEREST =4

class TerrainType(Enum):
    CLEAR         =1
    STEPPE        =2
    HILLS         =3
    MOUNTAINS     =4
    WOODS         =5
    WOODED_HILLS  =6
    STONY_HILLS   =7
    DESERT        =8
    SANDY_DESERT  =9
    STONY_DESERT  =10
    SALT_MARSH    =11

class FortificationType(Enum):
    MJR_FORT_HEXSIDE =1
    FORT_HEXSIDE     =2
    PORT_FORT        =3
    WORKS_1          =4
    WORKS_2          =5
    WORKS_3          =6
    WORKS_4          =7

class HexsideType(Enum):
    RIVER      =1
    CANAL      =2
    WADI       =3
    ESCARPMENT =4
    CLIFFS     =5
    MOUNTAIN   =6
