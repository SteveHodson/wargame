import random
import math
import logging

from src.tables.constants import Nation


class CombatTables():
   
    # create a singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CombatTables, cls).__new__(cls)
        return cls.instance

    def ground_cev(self, year: str, nation: Nation):
        try:
            ground_cev_table = {
                '1941': {Nation.GERMANY: 1.5, Nation.ITALY: 1, Nation.ALLIED: 1.3}
            }
            return ground_cev_table[year][nation]
        except KeyError as e:
            logging.error('Wrong year used')
            raise KeyError('Wrong Year Used')


    def ground_combat_resolution_table(self, attack, defence,drm: int, seed=None):
        combat_results_code = ['AE','AH','AQ','HR','QR','HQ','DR','QH','EX','HX','DQ','DH','DE','DA']
        
        random.seed(seed)
        modded_roll = random.randint(1,10) + drm + 4 # scaling to zero for the modded roll
        
        if modded_roll < 0: modded_roll = 0
        if modded_roll > 20: modded_roll = 20

        self.combat_odds_index = self._ratio(attack, defence) #= combat_odds.index(self.odds)
        offset = modded_roll + self.combat_odds_index
        result_index = offset - 7
        if offset < 8: result_index = 0
        if offset > 19 and offset < 28: result_index = 12
        if offset > 27: result_index = 13
        
        return combat_results_code[result_index]
    
    def ground_cbt_result(self, cbt_code: str):
        try:
            grnd_cbt_results = {
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
                'DA': ('NE','Annihilated','None')
            }
            return grnd_cbt_results[cbt_code]
        except KeyError as e:
            logging.error('Combat code used')
            raise KeyError('Combat Code Used')

    # Return the index of the list of odd
    def _ratio(self, a, d, seed=None) -> int:
        if a == d: return 3
        random.seed(seed)
        r = random.randint(1,10)
        if a > d:
            ret = 2+math.ceil(a/d) if r > 5 else 2+math.floor(a/d)
            if ret > 8: ret = 8
            return ret
        if a < d:
            ret = 4 - math.ceil(d/a) if r > 5 else 4 - math.floor(d/a)
            if ret < 0: ret = 0
            return ret
