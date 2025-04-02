import random as r

#have multiple enemies for now 
class enemy():
    def __init__(self,baseA,baseH):
        self._baseA = r.uniform(0.0,10.0) + baseA
        self._baseH = r.uniform(0.0,10.0) + baseH
    def getatk(self):
        return self._baseA
    def gethp(self):
        return self._baseH
    def atk():
        pass
class zombieE(enemy):
    def __init__(self, baseA, baseH):
        super().__init__(baseA, baseH)
    def getatk(self):
        return super().getatk()
    def gethp(self):
        return super().getatk()
    def infection(self):
        zIn = r.uniform(0.0,3.0)
        return zIn
    

class banditE(enemy):
    def __init__(self, baseA, baseH):
        super().__init__(baseA, baseH)
    def getatk(self):
        return super().getatk()
    def gethp(self):
        return super().gethp()