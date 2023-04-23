import random, math

'''
Determine the results of Ground Combat
'''
class GroundCombatResults():

    def __init__(self, drm: int, attack:int, defence: int):
        self.drm = drm
        self.attack = attack
        self.defence = defence
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
            'DA': ('NE','Annihilated','None')
        }    

    def calculate_result(self):
        pass
        # combat_results_code = ['AE','AH','AQ','HR','QR','HQ','DR','QH','EX','HX','DQ','DH','DE','DA']
        # #combat_odds = ['1:4','1:3','1:2','1:1','2:1','3:1','4:1','5:1','6:1','7:1','8:1','9:1']

        # modded_roll = _dice(10) + self.drm + 4 # scaling to zero for the modded roll
        # if modded_roll < 0: modded_roll = 0
        # if modded_roll > 20: modded_roll = 20
        # print(f'Die Roll: {modded_roll-4-self.drm}')

        # self.combat_odds_index = _ratio(self.attack, self.defence) #= combat_odds.index(self.odds)
        # offset = modded_roll + self.combat_odds_index
        # result_index = offset - 7
        # if offset < 8: result_index = 0
        # if offset > 19 and offset < 28: result_index = 12
        # if offset > 27: result_index = 13
        
        # return combat_results_code[result_index]

    def get_results(self):
        result = self.calculate_result()
        print(result)
        return self.results.get(result)



#if __name__ == "__main__":
    # random.seed()
    # for i in range(1,10):
    #     drm = random.randint(-2,3)
    #     attack = random.randint(1,25)
    #     defence = random.randint(1,20)
    #     odds = f'{attack}:{defence}'
    #     print('========================')
    #     print(f'Attack:Defence {odds} - drm: {drm}')
    #     print(_ratio(attack, defence))
    #     print(f'Results: {GroundCombatResults(drm, attack, defence).get_results()}')