from tkinter import *
from WarUnit import *
from Missile import *

class Vehicle(WarUnit):
    cost = 500
    active = 0
    def __init__(self,dir,x,y,speed,range,imgList,attackList,cost):
        super().__init__(dir,x,y,speed,range,imgList,attackList,cost)
        self.missile = None
        
      
    def checkHit(self,other):
        if other != None and self.getDisBetweenObj(other) < self.range:
            self.state =1
            if self.missile == None:
                #                       x,       y,   dir, attack
                
                
                self.missile = Missile(self.x,self.y,self.dir,20)

            # can only attack one once
            return True
            
        else:self.state = 0 