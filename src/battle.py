from data.hex import Hex
from data.unit import *
from tables.constants import *


# reader in from file
att_hex = Hex('0909',TerrainType.DESERT)
def_hex = Hex('1010', TerrainType.DESERT)

# 132 Ariete Armoured Division
att_u1 = GroundUnit(name='5/8B/132',size=GroundUnitSize.BATTALION,type=GroundUnitType.INFANTRY,mp=4,at=2,df=3,type_additional=GroundUnitTypeAdditional.MOTORISED)
att_u2 = GroundUnit(name='7/132/132',size=GroundUnitSize.BATTALION,type=GroundUnitType.ARMOUR,mp=4,at=10)
att_u3 = GroundUnit(name='1/132/132',size=GroundUnitSize.BATTALION,type=GroundUnitType.ARTILLERY,mp=4,at=7)
att_stack = GroundUnitStack(att_hex)
att_stack.make_active(att_u1)
att_stack.make_active(att_u2)
att_stack.make_active(att_u3)

def_u1 = GroundUnit(name='4th/11th Sikh',size=GroundUnitSize.BATTALION,type=GroundUnitType.INFANTRY,mp=5,at=6,df=7,type_additional=GroundUnitTypeAdditional.MOTORISED)
def_u2 = GroundUnit(name='Royal Sussex',size=GroundUnitSize.BATTALION,type=GroundUnitType.INFANTRY,mp=5,at=5,type_additional=GroundUnitTypeAdditional.MOTORISED)
def_u3 = GroundUnit(name='4th/16th Punjab',size=GroundUnitSize.BATTALION,type=GroundUnitType.INFANTRY,mp=5,at=5,type_additional=GroundUnitTypeAdditional.MOTORISED)
def_stack = GroundUnitStack(def_hex)
def_stack.make_active(def_u1)
def_stack.make_active(def_u2)
def_stack.make_active(def_u3)

print(att_stack.display_all())
print('====================')
print(def_stack.display_all())