import random as r

#have multiple enemies for now 
class enemy():
    def __init__(self,baseA,baseH):
        self._baseA = int(r.uniform(0.0,10.0) + baseA) #change for balancing
        self._baseH = int(r.uniform(0.0,10.0) + baseH)
    def getatk(self):
        return self._baseA
    def gethp(self):
        return self._baseH
    def atk(self):
        pass
class zombieE(enemy):
    def __init__(self, baseA, baseH):
        super().__init__(baseA, baseH)
    def getatk(self):
        return super().getatk()
    def gethp(self):
        return super().gethp()
    def infection(self):
        zIn = r.uniform(0.5,6.0) #total infection rate of player
        #print("Player's infection is now at:")
        return zIn
    def atk(self, player):
        player.take_damage(self._baseA, source=self)

    

class banditE(enemy):
    def __init__(self, baseA, baseH):
        super().__init__(baseA, baseH)
    def getatk(self):
        return super().getatk()
    def gethp(self):
        return super().gethp()
    def atk(self,player):
        player.take_damage(self._baseA,source=self)
