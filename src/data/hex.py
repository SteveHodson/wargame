from tables.constants import TerrainType, CityType, FortificationType, HexsideType


class Hex():
    def __init__(self, 
            coords: str, 
            terrain_type: TerrainType, 
            city_type: CityType=None,
            fort_type: FortificationType=None,
            hexside_type: HexsideType=None) -> None:
        
        self.coords = coords
        self.terrain_type = terrain_type
        self.city_type = city_type
        self.hexside_type = hexside_type
        self.fort_type = fort_type

    def get_terrain(self):
        return self.terrain_type

