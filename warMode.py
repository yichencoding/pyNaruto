import random
from tkinter import *
from Vehicle import *
from Building import *
from Missile import *
from Enemy import *
from Player import *
from WarUnit import *
from WarFrame import *



####################################
# war mode
####################################

def warMousePressed(event, data):
    pass

def warKeyPressed(event, data):
    if (event.keysym.lower() == 'h'):
        data.warHelp = 1-data.warHelp
        
    if data.warHelp==1:
        return
    else:
        deviation = random.uniform(-20, 40)
        soldierY = deviation+data.base.y
        if event.keysym == "1" and data.money>=WarUnit.cost:
            data.soldiers.add(WarUnit(1,data.base.x,soldierY,1,30,data.soldierList[0],data.soldierAttackList[0],100))
            data.money-=WarUnit.cost
        elif event.keysym == "2" and data.money>=WarUnit.cost:
            data.soldiers.add(WarUnit(1,data.base.x,soldierY,2,30,data.soldierList[1],data.soldierAttackList[1],100))
            data.money-=WarUnit.cost
        elif event.keysym == "3" and data.money>=WarUnit.cost:
            data.soldiers.add(WarUnit(1,data.base.x,soldierY,3,30,data.soldierList[2],data.soldierAttackList[2],100))
            data.money-=WarUnit.cost
        elif event.keysym == "4" and data.money>=WarUnit.cost:
            data.soldiers.add(WarUnit(1,data.base.x,soldierY,2,30,data.soldierList[3],data.soldierAttackList[3],100))  
            data.money-=WarUnit.cost  
        elif event.keysym == "5"and data.money>=Vehicle.cost:
            data.soldiers.add(Vehicle(1,data.base.x,soldierY,1,150,data.soldierList[4],data.soldierAttackList[4],500))
            data.money-=Vehicle.cost
            
def warTimerFired(data):
    if data.warHelp==1:
        return
    if data.warTimeCounter % 200 ==0:
        data.enemyMoveCount+=1
    if data.base.health<=0:
        data.mode = "gameOver"
    if data.enemyBase.health<=0:
        data.mode = "gameOver"
    calculateMoney(data)
    #data.player.state =0
    data.warTimeCounter+=data.timerDelay
    # Add enemies
    if data.warTimeCounter % 2000 ==0:
        choice = random.choice([0,1,2,3])
       
        deviation = random.uniform(-80, 40)
        enemyY = deviation+data.enemyBase.y
        if choice ==0:
        #                   dir, x ,  y     ,   speed, range
            data.warEnemies.add(WarUnit(-1,data.enemyBase.x,enemyY,1,20,data.enemyImgList[0],data.enemyAttackList[0],100))
        elif choice ==1:
            # iron man
            data.warEnemies.add(WarUnit(-1,data.enemyBase.x,enemyY,2,30,data.enemyImgList[1],data.enemyAttackList[1],100))
        elif choice ==2:
            # iron man
            data.warEnemies.add(WarUnit(-1,data.enemyBase.x,enemyY,3,40,data.enemyImgList[2],data.enemyAttackList[2],100))
        elif choice ==3:
            # iron man
            data.warEnemies.add(WarUnit(-1,data.enemyBase.x,enemyY,4,50,data.enemyImgList[3],data.enemyAttackList[3],100))
            
    moveSet(data.soldiers)
    moveSet(data.warEnemies)
            
    # Check attack            
    getAttack(data.soldiers,data.warEnemies,data.enemyBase)
    getAttack(data.warEnemies,data.soldiers,data.base)
    
    # checkMissile
    checkMissile(data.soldiers,data.warEnemies,data.enemyBase)
    checkMissile(data.warEnemies,data.soldiers,data.base)
    # Remove 
    removeUnit(data.warEnemies,data.money)
    removeUnit(data.soldiers, data.money)
    
def warRedrawAll(canvas, data):
    #BackGround
    canvas.create_image(data.width/2,data.height/2,image = data.backImg) 

    # Base
    canvas.create_image(data.width/2,data.height/2-70,image = data.warBack)
    
    data.base.draw(canvas,data)
    data.enemyBase.draw(canvas,data)
    # Animation
    for building in data.buildings:
        if building.state!=2:
            building.draw(canvas,data)
    for soldier in data.soldiers:
        soldier.draw(canvas,data)
        if  isinstance(soldier,Vehicle) and soldier.missile !=None:
            soldier.missile.draw(canvas,data)
        
        
    for warEnemy in data.warEnemies:
        warEnemy.draw(canvas,data)
        if  isinstance(warEnemy,Vehicle) and warEnemy.missile !=None:
            warEnemy.missile.draw(canvas,data)
    drawWarFrame(canvas,data)
    if data.warHelp==1:
        canvas.create_image(data.width/2,data.height/2,image = data.warHelpImg)
##################### Helper function
def numNeedRemove(set):
    num = 0
    for unit in set:
        if unit.health<=0:
            num+=1
    return num

def removeUnit(enemies,money):
    num = numNeedRemove(enemies)
    while num >0:
        for enemy in enemies:
            if enemy.health<=0:
                if enemy.dir==-1:
                    money += enemy.cost/2
                enemies.remove(enemy)
                num-=1
                break

def getAttack(selfSet,otherSet,base):
    for self in selfSet:
        if self.attackInterval>0:
            self.attackInterval-=1
        # No ememy
        if len(otherSet)<=0:
            # Check if can hit base
            if self.checkHit(base):
                continue# Skip the rest part, go to next soldider
            else:# No enemy, no available base, move 
                self.state = 0
        else:
            # Enemy remains, check if attack
            for other in otherSet:
                if self.checkHit(other):
                    break
def checkMissile(selfSet,otherSet,base):
    
    for other in otherSet:
        for self in selfSet:
            if isinstance(self,Vehicle):
                if self.missile!= None:
                    
                    if self.missile.hitEnemy(other):
                        self.missile= None
                    # Outside screen
                    elif self.missile.x<=0 or self.missile.x>=1080:
                        self.missile= None
    
    if len(otherSet) <= 0:
        for self in selfSet:
            if isinstance(self,Vehicle):
                if self.missile!= None:
                    if self.missile.hitEnemy(base):
                        self.missile = None
        
def moveSet(set):
    for unit in set:
        if unit.state == 0:
            unit.move()
        if isinstance(unit,Vehicle) and unit.missile!= None:
            unit.missile.move()
    