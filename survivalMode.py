####################################
# survival mode
####################################

import random
from tkinter import *
from Enemy import *
from Item import *
from Weapon import *
from Bandage import *
from Chakura import *
from Bullet import *
from SurvivalFrame import *
from Collection import *

def survivalMousePressed(event, data):
    data.player.playerShoot(data,event.x,event.y)

def survivalKeyPressed(event, data):
    if (event.keysym.lower() == 'h'):
        data.survivalHelp = 1-data.survivalHelp
        
    if data.survivalHelp==1:
        return
    # Abilities 
    if event.keysym.lower() == "j" and data.player.abilityJTime==0 and data.player.magic>20 and data.player.level>0:
        data.player.abilityJTime=1
        data.player.magic-=20
    if event.keysym.lower() == "k" and data.player.abilityKTime==0 and data.player.magic>30 and data.player.level>1:
        data.player.abilityKTime=1
        data.player.magic-=30
    if event.keysym.lower() == "l" and data.player.abilityLTime==0 and data.player.magic>40 and data.player.level>2:
        data.player.abilityLTime=1
        data.player.magic-=40
     
    if event.keysym.lower() == "w" and data.scrollY<data.survivalHeight/2:
        data.moveCount+=1
        if checkLegal(data.player.x-data.scrollX,data.player.y-(data.scrollY+5),data.blocks):
            data.scrollY +=5
        data.player.direction = "up"
    if event.keysym.lower() == "a" and data.scrollX<data.survivalWidth/2:
        if checkLegal(data.player.x-(data.scrollX+5),data.player.y-data.scrollY,data.blocks):
            data.scrollX +=5
        data.player.direction = "left"
        data.moveCount+=1
    if event.keysym.lower() == "s" and data.scrollY>-data.survivalHeight/2:
        if checkLegal(data.player.x-data.scrollX,data.player.y-(data.scrollY-5),data.blocks):
            data.scrollY -=5
        data.player.direction = "down"
        data.moveCount+=1
    if event.keysym.lower() == "d" and data.scrollX>-data.survivalWidth/2:
        if checkLegal(data.player.x-(data.scrollX-5),data.player.y-data.scrollY,data.blocks):
            data.scrollX -=5
        data.player.direction = "right"
        data.moveCount+=1
    if event.keysym == "space" and data.attackInterval==0:
        
        data.player.state = 1
        data.attackInterval=5
        for enemy in data.enemies:
            data.player.playerAttack(enemy,data)
            
    if event.keysym.lower() == "f" :
        for collection in data.collections:
            data.player.getCollection(collection,data)
        data.player.playerPickItem(data.items,data)
        
    if event.keysym.lower() =="i":
        data.bag = 1-data.bag
        #data.prevMode = data.mode    
        
        #data.mode = "help"
    
def survivalTimerFired(data):
    if data.survivalHelp==1:
        return
    if data.player.magic<=100:
        data.player.magic+=1
    #print(data.player.abilityJTime)
    for enemy in data.enemies:
        data.player.playerJAttack(enemy,data)
    for enemy in data.enemies:
        data.player.playerKAttack(enemy,data)
    for enemy in data.enemies:
        data.player.playerLAttack(enemy,data)
    
    
    
    # Player level up
    if data.player.exp>=100:
        data.player.level+=1
        data.player.exp=0
    # Ability J
    if data.player.abilityJTime==data.abilityJNum/2:
        data.player.abilityJTime=0
    if 0<data.player.abilityJTime<data.abilityJNum/2:
        data.player.abilityJTime+=1
    # Ability K
    if data.player.abilityKTime==data.abilityKNum/2:
        data.player.abilityKTime=0
    if 0<data.player.abilityKTime<data.abilityKNum/2:
        data.player.abilityKTime+=1
    # Ability L
    if data.player.abilityLTime==data.abilityLNum/2:
        data.player.abilityLTime=0
    if 0<data.player.abilityLTime<data.abilityLNum/2:
        data.player.abilityLTime+=1

    

    if data.player.health<=0:
        data.mode="gameOver"
    if len(data.collections) == 0:
        
        
        # First
        x = random.uniform(-(data.survivalWidth/2-data.width/2), data.width+data.survivalWidth/2-data.width/2)
        y = random.uniform(-(data.survivalHeight/2-data.height/2),data.height+data.survivalHeight/2-data.height/2)
        
        while True:
            if checkLegal(x,y,data.blocks):
                data.collections.add(Collection(x,y,data.width-50,data.height-50,
                                data.ironImg))
                break
               
            x = random.uniform(-(data.survivalWidth/2-data.width/2), data.width+data.survivalWidth/2-data.width/2)
            y = random.uniform(-(data.survivalHeight/2-data.height/2),data.height+data.survivalHeight/2-data.height/2)
        # Second
        x = random.uniform(-(data.survivalWidth/2-data.width/2), data.width+data.survivalWidth/2-data.width/2)
        y = random.uniform(-(data.survivalHeight/2-data.height/2),data.height+data.survivalHeight/2-data.height/2)
        
        while True:
            if checkLegal(x,y,data.blocks):
                data.collections.add(Collection(x,y,data.width-150,data.height-50,
                                data.spiderImg))
                break
               
            x = random.uniform(-(data.survivalWidth/2-data.width/2), data.width+data.survivalWidth/2-data.width/2)
            y = random.uniform(-(data.survivalHeight/2-data.height/2),data.height+data.survivalHeight/2-data.height/2)
        # Third
        x = random.uniform(-(data.survivalWidth/2-data.width/2), data.width+data.survivalWidth/2-data.width/2)
        y = random.uniform(-(data.survivalHeight/2-data.height/2),data.height+data.survivalHeight/2-data.height/2)
        
        while True:
            if checkLegal(x,y,data.blocks):
                data.collections.add(Collection(x,y,data.width-50,data.height-150,
                                data.capitalImg))
                break
               
            x = random.uniform(-(data.survivalWidth/2-data.width/2), data.width+data.survivalWidth/2-data.width/2)
            y = random.uniform(-(data.survivalHeight/2-data.height/2),data.height+data.survivalHeight/2-data.height/2)
        # Last
        x = random.uniform(-(data.survivalWidth/2-data.width/2), data.width+data.survivalWidth/2-data.width/2)
        y = random.uniform(-(data.survivalHeight/2-data.height/2),data.height+data.survivalHeight/2-data.height/2)
        
        while True:
            if checkLegal(x,y,data.blocks):
                data.collections.add(Collection(x,y,data.width-150,data.height-150,
                                data.wolverineImg))
                break
               
            x = random.uniform(-(data.survivalWidth/2-data.width/2), data.width+data.survivalWidth/2-data.width/2)
            y = random.uniform(-(data.survivalHeight/2-data.height/2),data.height+data.survivalHeight/2-data.height/2)
            
    if data.timeCounter % 200 ==0:
        # Foe moving animation
        data.enemyMoveCount+=1
    
    for collection in data.collections:
        data.player.getCollection(collection,data)
    
    if checkCompletion(data.collections):
        data.mode = "war"
    if data.attackInterval>0:
        data.attackInterval-=1
    data.player.state =0
    data.timeCounter+=data.timerDelay
    # Enemies and items can't collide with blocks
    if data.timeCounter % 1000 ==0 and len(data.enemies)<15:
        

        x = random.uniform(0, data.width)
        y = random.uniform(0, data.height)
        
        while True:
            if checkLegal(x,y,data.blocks):
                data.items.add(Weapon(x,y,10,data.gunImg))
                break
               
            x = random.uniform(0, data.width)
            y = random.uniform(0, data.height)
        
        while True:
            if checkLegal(x,y,data.blocks):
                index = random.choice([0,1,2,3])
                #list = random.choice(data.enemyImgList)
                data.enemies.add(Enemy(x,y,data.enemyImgList[index],data.enemyAttackList[index]))
                break
               
            x = random.uniform(0, data.width)
            y = random.uniform(0, data.height)
    for enemy in data.enemies:
        
        enemy.move(data.player,data)
        enemy.checkAttack(data.player,data)
    removeEnemy(data.enemies,data)
    for bullet in data.bullets:
        bullet.move()

    for enemy in data.enemies:
        for bullet in data.bullets:
            if bullet.hitEnemy(enemy):
                data.bullets.remove(bullet)
                break

            
            
                       
    removeBullet(data.bullets,data)
    

    
def survivalRedrawAll(canvas, data):
    # Background
    canvas.create_image(data.width/2+data.scrollX,data.height/2+data.scrollY ,image = data.edgeImg)
    canvas.create_image(data.width/2+data.scrollX,data.height/2+data.scrollY ,image = data.survivalBack)
    
    for block in data.blocks:
        block.draw(canvas,data)
    # Items
    for item in data.items:
        item.draw(canvas,data)
    # Enemy
    for enemy in data.enemies:
        enemy.draw(canvas,data)
    # Player
    data.player.drawPlayer(canvas,data) 
    # Bullet
    for bullet in data.bullets:
        bullet.draw(canvas,data)
        
    for collection in data.collections:
        collection.draw(canvas,data)
    
    
    drawSurvivalFrame(canvas,data)

    canvas.create_image(data.statusImage.width()/2,data.statusImage.height()/2,image = data.statusImage)
    if data.bag == 1:
        bagWid = data.bagImg.width()
        bagHei = data.bagImg.height()     
        canvas.create_image(data.width-bagWid/2,data.height-bagHei/2,image = data.bagImg)
        for collection in data.collections:
            if collection.collected ==1:
                canvas.create_image(collection.sx,collection.sy,image = collection.image)
    
    if data.survivalHelp==1:
        canvas.create_image(data.width/2,data.height/2,image = data.survivalHelpImg)
    
    
############################# helper functions 







def checkCompletion(collections):
    for collection in collections:
        if collection.collected == 0:
            return False
    return True

   
def numNeedRemove(enemies):
    num = 0
    for enemy in enemies:
        if enemy.health<=0: 
            num+=1
    return num
        

def removeEnemy(enemies,data):
    num = numNeedRemove(enemies)

    while num >0:
        for enemy in enemies:
            if enemy.health<=0:
                chance = random.choice([0,1,2,3])
                if chance ==1:
                    data.items.add(Bandage(enemy.x,enemy.y,10,data.bandageImg))
                elif chance ==2:

                    data.items.add(Chakura(enemy.x,enemy.y,10,data.chakuraImg))
                data.player.exp+=50
                enemies.remove(enemy)
                num-=1
                break
                
def removeBullet(bullets,data):
    for bullet in bullets:
        if not (0<bullet.x+data.scrollX<data.width and \
                0<bullet.y+data.scrollY<data.height) :
            bullets.remove(bullet)
            break

def checkLegal(x,y,blocks):
    for block in blocks:
        if abs(x-block.x)<(block.width+64)/2 and \
           abs(y-block.y)<(block.height + 100)/2:
               return False
    return True


def insideBlock(x,y,block):
        if abs(x-block.x)<(block.width+64)/2 and \
           abs(y-block.y)<(block.height + 100)/2:
               return True
        return False