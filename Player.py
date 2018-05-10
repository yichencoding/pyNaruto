import random
import math
from Bullet import *
from Weapon import *
from Bandage import *
from Chakura import *

class Player(object):
    fullHealth = 100
    def __init__(self,data,playerImgList):
        
        self.x = data.width/2
        self.y = data.height/2
        self.speed = 2
        self.width = 64
        self.height = 80
        self.health = 100
        self.magic = 100
        self.playerImgList = playerImgList
        #self.playerAttackImg = playerAttackImg
        self.state = 0
        self.attack = 10
        self.gun = None
        self.direction = "left"
        self.item = set()
        # J ability works for level>=1
        self.abilityJTime = 0
        # K ability works for level>=2
        self.abilityKTime = 0
        # L ability works for level>=3
        self.abilityLTime = 0
        self.level = 0
        self.exp = 0
        
        
        
        
    def setPosition(self,x,y):
        self.x = x
        self.y = y
        
        
    def drawPlayer(self,canvas,data):
        # Body
        
        #if self.state == 0 :# Move
        if data.attackInterval==0:
            if self.direction == "left":
                start = 1
            elif self.direction == "right":
                start =2
            elif self.direction == "up":
                start=3
            elif self.direction == "down":
                start = 0
            img = self.playerImgList[start*4+data.moveCount%4]
        elif data.attackInterval>0:
            # Attacking 
            if self.direction in ["left","up"]:
                img = data.soldierAttackList[0][5-data.attackInterval]
                #img = self.playerImgList[-2]
            if self.direction in ["right","down"]:
                #img = self.playerImgList[-1]
                img = data.soldierAttackList[0][10-data.attackInterval]
        # Abilities               
        if self.abilityJTime >0 and self.level>0:
            if self.direction in ["right","down"]:
                
                img = data.abilityJImg[self.abilityJTime-1]
            elif self.direction in ["left","up"]:
                img = data.abilityJImg[data.abilityJNum-self.abilityJTime]
            
            
        elif self.abilityKTime >0 and self.level>1:
            if self.direction in ["right","down"]:
                img = data.abilityKImg[self.abilityKTime-1]
            elif self.direction in ["left","up"]:
                img = data.abilityKImg[data.abilityKNum-self.abilityKTime]
                
        elif self.abilityLTime >0 and self.level>1:
            if self.direction in ["right","down"]:
                img = data.abilityLImg[self.abilityLTime-1]
            elif self.direction in ["left","up"]:
                img = data.abilityLImg[data.abilityLNum-self.abilityLTime]
                
        canvas.create_image(self.x,self.y,image = img)
        
        
        # Weapon
        if self.gun !=None:
            canvas.create_image(40,200,image = data.gunImg)
            canvas.create_text(110, 200,
                       text="X " +str(data.player.gun.ammo),fill="black", font="fixedsys 30 bold")
            

    
    def playerPickItem(self,items,data):
        for item in items:
            dis = self.getDisBetweenObj(item,data)

            if dis < (self.width)**2:
                # Pick up weapon
                if isinstance(item,Weapon):
                    self.gun = item
                    items.remove(item)
                    break
                # Pick up bandage
                if isinstance(item,Bandage):
                    health = self.health + 20
                    if health>=100:
                        self.health = 100
                    else:
                        
                        self.health+=20
                    items.remove(item)
                    break
                if isinstance(item,Chakura):
                    magic = self.magic + 20
                    if magic>=100:
                        self.magic = 100
                    else:
                        
                        self.magic+=20
                    items.remove(item)
                    break
    
    def playerJAttack(self,enemy,data):
        attackJ = 20
        mp = 20
        dis = self.getDisBetweenObj(enemy,data)
        if dis < (100)**2 and self.abilityJTime ==data.abilityJNum/2-1:
            enemy.health -= attackJ
            
            
    def playerKAttack(self,enemy,data):
        attackK = 30
        mp = 30
        dis = self.getDisBetweenObj(enemy,data)
        if dis < (100)**2 and self.abilityKTime ==data.abilityKNum/2-1:
            enemy.health -= attackK
            
    def playerLAttack(self,enemy,data):
        attackL = 40
        mp = 40
        dis = self.getDisBetweenObj(enemy,data)
        if dis < (100)**2 and self.abilityLTime ==data.abilityLNum/2-1:
            enemy.health -= attackL

            
    def playerAttack(self,enemy,data):
        dis = self.getDisBetweenObj(enemy,data)
        
        if dis < (self.width)**2 and self.state ==1:

            enemy.health -= self.attack
    
    def getDir(self,data,x,y):
        deltaX = x-self.x
        deltaY = y-self.y
        dis = math.sqrt(deltaX **2 + deltaY **2)
        if deltaX > 0:dx = 1  
        else:dx = -1
        if deltaY >0:dy = 1
        else:dy = -1
        dir = math.asin(deltaY/dis)
        return dx,dy,dir
        
    def playerShoot(self,data,x,y):
        if self.gun != None and self.gun.ammo >0:
            (dx,dy,dir) = self.getDir(data,x,y)
            data.bullets.add(Bullet(self.x+self.gun.image.width()/2-data.scrollX,self.y  -data.scrollY,
                                    dx,dy,abs(dir),self.gun.attack))
            self.gun.ammo-=1
            if self.gun.ammo == 0:
                self.gun =None
    
    def getDisBetweenObj(self,other,data):
        deltaX = other.x+data.scrollX-self.x
        deltaY = other.y+data.scrollY-self.y
        dis = deltaX **2 + deltaY **2
        return dis
    
    def getCollection(self,other,data):
        deltaX = other.x+data.scrollX-self.x
        deltaY = other.y+data.scrollY-self.y
        dis = math.sqrt(deltaX **2 + deltaY **2)
        if dis<=self.width/2:
            other.collected = 1