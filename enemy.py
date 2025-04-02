import random as r

#have multiple enemies for now 
class enemy():
    def __init__(self,baseA,baseH):
        self._baseA = int(r.uniform(0.0,10.0) + baseA)
        self._baseH = int(r.uniform(0.0,10.0) + baseH)
    def getatk(self):
        return self._baseA
    def gethp(self):
        return self._baseH
    def atk(self,playerH):
        pass
class zombieE(enemy):
    def __init__(self, baseA, baseH):
        super().__init__(baseA, baseH)
    def getatk(self):
        return super().getatk()
    def gethp(self):
        return super().getatk()
    def infection(self,cinfect):
        zIn = r.uniform(0.0,3.0) + cinfect #total infection rate of player
        #print("Player's infection is now at:")
        return zIn
    def atk(self,playerH,cinfect):
        playerH = playerH - self._baseA
        if(r.random() > 0.5):
            infection(cinfect) # type: ignore
        #print("Player health now at:",playerH)
        return playerH
    

class banditE(enemy):
    def __init__(self, baseA, baseH):
        super().__init__(baseA, baseH)
    def getatk(self):
        return super().getatk()
    def gethp(self):
        return super().gethp()
