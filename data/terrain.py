from data.units import GroundUnitTypeAdditional

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