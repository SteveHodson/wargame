from src.tables.constants import GroundUnitTypeAdditional,TerrainType,HexsideType,FortificationType


class Hex():

    # create a singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Hex, cls).__new__(cls)
        return cls.instance

    def effects_modifer(self, terrain_type: TerrainType, unit_type: GroundUnitTypeAdditional):
        effects = self._ground_unit_effects(terrain_type)
        if unit_type == GroundUnitTypeAdditional.OTHERS:
            effects.pop(GroundUnitTypeAdditional.MOTORISED)
        else:
            effects.pop(GroundUnitTypeAdditional.OTHERS)
        return effects

    def _city_types(self):
        pass
    def _fortification_types(self, fort_type: FortificationType):
        fort_types = {
            FortificationType.MJR_FORT_HEXSIDE: {'drm':  -1, 'ASE': 0.5,  GroundUnitTypeAdditional.MOTORISED: (1.0,2), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            FortificationType.FORT_HEXSIDE:     {'drm':  -1, 'ASE': 0.5,  GroundUnitTypeAdditional.MOTORISED: (1.0,2), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            FortificationType.PORT_FORT:        {'drm':  -1, 'ASE': 0.75, GroundUnitTypeAdditional.MOTORISED: (1.0,2), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            FortificationType.WORKS_1:          {'drm':  -1, 'ASE': 0.75, GroundUnitTypeAdditional.MOTORISED: (0.75,1), GroundUnitTypeAdditional.OTHERS: (1.0,1)},
            FortificationType.WORKS_2:          {'drm':  -1, 'ASE': 0.75, GroundUnitTypeAdditional.MOTORISED: (0.75,1), GroundUnitTypeAdditional.OTHERS: (1.0,1)},
            FortificationType.WORKS_3:          {'drm':  -1, 'ASE': 0.75, GroundUnitTypeAdditional.MOTORISED: (0.75,1), GroundUnitTypeAdditional.OTHERS: (1.0,1)},
            FortificationType.WORKS_4:          {'drm':  -1, 'ASE': 0.75, GroundUnitTypeAdditional.MOTORISED: (0.75,1), GroundUnitTypeAdditional.OTHERS: (1.0,1)}
        }
        return fort_types[fort_type]
    def _terrain_hexsides(self, hexside_type: HexsideType):
        terrain_hexsides = {
            HexsideType.RIVER:      {'drm':  -1, 'ASE': 0.5,  GroundUnitTypeAdditional.MOTORISED: (1.0,2), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            HexsideType.CANAL:      {'drm':  -1, 'ASE': 0.5,  GroundUnitTypeAdditional.MOTORISED: (1.0,2), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            HexsideType.WADI:       {'drm':  -1, 'ASE': 0.75, GroundUnitTypeAdditional.MOTORISED: (1.0,2), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            HexsideType.ESCARPMENT: {'drm':  -1, 'ASE': 0.75, GroundUnitTypeAdditional.MOTORISED: (0.75,1), GroundUnitTypeAdditional.OTHERS: (1.0,1)},
            HexsideType.CLIFFS:     {'drm':  -1, 'ASE': 0.75, GroundUnitTypeAdditional.MOTORISED: (0.75,1), GroundUnitTypeAdditional.OTHERS: (1.0,1)},
            HexsideType.MOUNTAIN:   {'drm':  -1, 'ASE': 0.5,  GroundUnitTypeAdditional.MOTORISED: (0.5,2), GroundUnitTypeAdditional.OTHERS: (0.75,1)}
        }
        return terrain_hexsides[hexside_type]

    def _ground_unit_effects(self, terrain_type: TerrainType):
        # tuples are (cbt_mod, mp_mod)
        ground_unit_effects = {
            TerrainType.CLEAR:        {'drm':  0, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.25,1), GroundUnitTypeAdditional.OTHERS: (1.0,1)},
            TerrainType.STEPPE:       {'drm':  0, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.50,1), GroundUnitTypeAdditional.OTHERS: (1.0,1)},
            TerrainType.HILLS:        {'drm': -1, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.25,2), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            TerrainType.MOUNTAINS:    {'drm': -2, 'ASE': 'N', GroundUnitTypeAdditional.MOTORISED: (0.50,4), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            TerrainType.WOODS:        {'drm': -1, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.00,2), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            TerrainType.WOODED_HILLS: {'drm': -2, 'ASE': 'H', GroundUnitTypeAdditional.MOTORISED: (1.00,3), GroundUnitTypeAdditional.OTHERS: (1.0,3)},
            TerrainType.STONY_HILLS:  {'drm': -1, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.00,2), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            TerrainType.DESERT:       {'drm':  0, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.50,1), GroundUnitTypeAdditional.OTHERS: (1.0,1)},
            TerrainType.SANDY_DESERT: {'drm':  0, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.25,3), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            TerrainType.STONY_DESERT: {'drm':  0, 'ASE': 'Y', GroundUnitTypeAdditional.MOTORISED: (1.15,3), GroundUnitTypeAdditional.OTHERS: (1.0,2)},
            TerrainType.SALT_MARSH:   {'drm': -5, 'ASE': 'N', GroundUnitTypeAdditional.MOTORISED: (0.10,10),GroundUnitTypeAdditional.OTHERS: (0.1,6)}
        }
        return ground_unit_effects[terrain_type]