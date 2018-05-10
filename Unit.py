import math

class Unit(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        # state = 0 means walk
        # State = 1 shooting
        self.state = 0
        self.cost = 0
        self.mis = None
        

        
    def checkShoot(self,building):
        # If unit is close to enemy, then stop and shoot
        if (building.x-self.x)**2 + (building.y-self.y)**2 < (self.range+building.size) **2 and\
            self.state == 0 :

            self.state = 1
    
    def move(self):
        self.x += self.speed   
    def draw(self,canvas):
        pass
    
    def getDisBetweenObj(self,other):
        deltaX = other.x-self.x
        deltaY = other.y-self.y
        return deltaX **2 + deltaY **2
        
        
# Out of screen, remove        
def removeUnit(set,data):
    for element in set:
        if element.x>data.width:
            set.remove(element)
            break
            


    