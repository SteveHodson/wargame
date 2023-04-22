import random

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

def _dice(n):
    random.seed()
    return random.randint(1,n)


if __name__ == "__main__":
    print(GroundCombatResults(-2, '5:1').get_effects())