
###################################################################
"""
citation
graphic resources:
purchased in https://sucaiwangguo.taobao.com/
sprite sheet:https://jordwilf.deviantart.com/art/Young-Naruto-shinobi-rumble-progress-sheet-1-292211468


"""
import random
from tkinter import *
from Weapon import *
from Bandage import *
from Chakura import *
from Block import *

from Vehicle import *
from Building import *
from Missile import *
from Enemy import *
from Player import *
from Item import *
from Bullet import *
from SurvivalFrame import *
#### import mode 
from helpMode import *
from splashScreenMode import *
from warMode import *
from setUpMode import *
from aboutMode import *
#from gameOverMode import * 
from survivalMode import *
from Collection import *

###################################################################
# From mode demo
####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    loadImages(data)
    # For help mode
    data.page = 0
    data.mode = "splashScreen"
    data.prevMode = "splashScreen"
    data.currentBlock =None
    # For menu
    data.blockWid = 100
    data.blockHei = 50
    data.playX = data.width/2
    data.playY = data.height/5
    data.helpX = data.width/2
    data.helpY = data.height/5 * 2
    data.aboutX = data.width/2
    data.aboutY = data.height/5*3
    data.setUpHelp =0
    data.survivalHelp = 0
    data.bag = 0
    # Stuff for both
    data.money =2000
    data.lineHeight = 4*data.height/5
    data.attackInterval = 0
    data.realTime =0
    # Survival stuff
    data.blocks = set()
    data.enemyMoveCount = 0
    data.moveCount=-1
    data.scrollX = 0
    data.scrollY = 0
    data.scrollMargin = 50
    data.player = Player(data,data.playerImgList)
    margin = 50
    data.survivalWidth = data.survivalBack.width()
    data.survivalHeight = data.survivalBack.height()
    data.enemies = set()
    data.items = set()
    data.bullets = set()
    data.chosenBlock = None
    data.collections = set()
    # Frame stuff
    data.margin = 20
    data.blockSize = 100

    # For war mode
    data.warHelp = 0
    data.base = Building(data.baseImg.width()/2,
                         data.lineHeight-data.baseImg.height()/2,
                         data.baseImg)
    data.enemyBase = Building(data.width - data.enemyBaseImg.width()/2,
                              data.lineHeight-data.enemyBaseImg.height()/2,
                              data.enemyBaseImg)
    data.soldiers = set()
    data.buildings = set()
    data.moneyspeed = 5
    
    data.timeCounter = 0
    data.warTimeCounter = 0
    data.warEnemies = set()
    

####################################
# helper functions
####################################


def loadImages(data):
    data.menuBlockImg =  PhotoImage(file= "image/menuBlock.gif")
    # For help
    data.helpImg = PhotoImage(file= "image\\helpBack.gif")
    ################## For survival
    data.playerImgList =getSpriteImage("naruto")
    data.enemyImgList =[getSpriteImage("woailuo"),getSpriteImage("kanjiulang"),getSpriteImage("zaibuzhan"),getSpriteImage("brother")]
    data.soldierList =[getSpriteImage("naruto"),getSpriteImage("sasuke"),getSpriteImage("sakura"),getSpriteImage("kakaxi"),getSpriteImage("lee")]
    #Ability
    data.abilityJNum = 5*2
    data.abilityJImg = getSkillImage("j",data.abilityJNum)
    data.abilityKNum = 5*2
    data.abilityKImg = getSkillImage("k",data.abilityKNum)
    data.abilityLNum = 9*2
    data.abilityLImg = getSkillImage("l",data.abilityLNum)


    data.setUpHelpImg=PhotoImage(file= "image/setUpHelp.gif")
    data.setUpFrameImg =PhotoImage(file= "image/setUpFrame.gif")
    data.warHelpImg = PhotoImage(file= "image/warHelp.gif")

    # For status
    data.attackStatus0Img = PhotoImage(file= "image/attackStatus.gif")
    data.attackStatus1Img = PhotoImage(file= "image/attackStatus1.gif")
    data.attackStatus2Img = PhotoImage(file= "image/attackStatus2.gif")
    data.attackStatus3Img = PhotoImage(file= "image/attackStatus3.gif")
    data.statusImage = PhotoImage(file= "image/status.gif")

    data.bagImg = PhotoImage(file= "image/bag.gif")
    
    data.survivalBack =PhotoImage(file= "image\survivalBack.gif")
    data.survivalHelpImg = PhotoImage(file= "image\survivalHelp.gif")
    data.gunImg = PhotoImage(file="image\gun.gif")
    data.backImg = PhotoImage(file="image\splashScreenBack.gif")
    data.bandageImg = PhotoImage(file="image/bandage.gif")
    data.chakuraImg = PhotoImage(file="image/chakura.gif")
    data.splashBackImg = PhotoImage(file = "image\splashScreenBack.gif")
    data.frameBack = PhotoImage(file = "image\\frameBack.gif")
    data.frameBlockImg = PhotoImage(file = "image/frameBlock.gif")
    data.weaponImg = PhotoImage(file = "image/weaponImg.gif")
    data.survivalFrameImg = PhotoImage(file = "image/survivalFrame.gif")
    # Collections
    data.spiderImg = PhotoImage(file= "image/collections/green.gif")
    data.ironImg = PhotoImage(file= "image/collections/blue.gif")
    data.capitalImg = PhotoImage(file= "image/collections/purple.gif")
    data.wolverineImg = PhotoImage(file= "image/collections/orange.gif")
    ###################  For war 
    data.warBack = PhotoImage(file="image\warBack.gif")
    data.baseImg = PhotoImage(file= "image\\base.gif")
    data.enemyBaseImg = PhotoImage(file= "image\enemyBase.gif")
    data.soldierAttackList = [getSkillImage("narutoAttack",10),getSkillImage("sasukeAttack",10),getSkillImage("sakuraAttack",10),getSkillImage("kakaxiAttack",10),getSkillImage("leeAttack",10)]
    data.enemyAttackList =[getSkillImage("woailuoAttack",10),getSkillImage("kanjiulangAttack",10),getSkillImage("zaibuzhanAttack",10),getSkillImage("brotherAttack",10)]
    #data.tankImg = PhotoImage(file= "image\\tank.gif")
    #data.tankRevImg = PhotoImage(file= "image\\tankReverse.gif")
    
    data.edgeImg = PhotoImage(file= "image\\edge.gif")
    
    data.headsImg = [PhotoImage(file= "image/head/naruto.gif"),PhotoImage(file= "image/head/sasuke.gif"),PhotoImage(file= "image/head/sakura.gif"),PhotoImage(file= "image/head/kakaxi.gif"),PhotoImage(file= "image/head/lee.gif")]
    
    ############### For gameOver
    data.gameOverBack = PhotoImage(file= "image\gameOverBack.gif") 
    data.bulletImg = PhotoImage(file= "image\\bullet.gif") 
    data.missileImg = PhotoImage(file= "image/missile.gif") 
    data.blockImg = PhotoImage(file= "image/block.gif")
    data.tallImg = PhotoImage(file= "image/tallBlock.gif")
    data.longImg = PhotoImage(file= "image/longBlock.gif")

    ################ For about
    data.aboutImg = PhotoImage(file= "image/about.gif")


    
def getSpriteImage(folder,total = 16):
    #total = 16
    list=[]
    for index in range(total):
        list+= [PhotoImage(file= folder + "/"+folder+ " (%d).gif"%(index+1))]
    list+= [PhotoImage(file= folder + "/"+"leftAttack.gif")]    
    list+= [PhotoImage(file= folder + "/"+"rightAttack.gif")]      
    return list
    
    
def getSkillImage(folder,total = 16):
    #total = 16
    list=[]
    for index in range(total):
        list+= [PhotoImage(file= folder + "/"+folder+ " (%d).gif"%(index+1))]
    return list
    
    
    

####################################
# gameOver mode
# This mode is not separated since it calls init to reinitialize everything
####################################

#from main import init
def gameOverMousePressed(event,data):
    pass

def gameOverKeyPressed(event,data):
    if event.keysym.lower() == "r":
        init(data)
        data.mode ="splashScreen"

def gameOverTimerFired(data):
    pass
def gameOverRedrawAll(canvas,data):
    
    canvas.create_image(data.width/2, data.height/2,image = data.gameOverBack)
    canvas.create_text(data.width/2, data.height/2,
                       text="Press 'r' to restart!", fill="white",font="fixedsys 30")
    if data.player.health <= 0 or data.base.health<=0:
        canvas.create_text(data.width/2, data.height/2-50,
                       text="Game Over!", fill="white",font="fixedsys 30")
    else:
        canvas.create_text(data.width/2, data.height/2-50,
                       text="You Win!",fill="white", font="fixedsys 30")

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "splashScreen"): splashScreenMousePressed(event, data)
    elif (data.mode == "survival"): survivalMousePressed(event, data)
    elif (data.mode == "setUp"):      setUpMousePressed(event, data)
    elif (data.mode == "war"):   warMousePressed(event, data)
    elif (data.mode == "help"):       helpMousePressed(event, data)
    elif (data.mode == "gameOver"):   gameOverMousePressed(event, data)
    elif (data.mode == "about"):   aboutMousePressed(event, data)
    

def keyPressed(event, data):
    if event.keysym.lower() == "q":
        data.mode = "war"
    if event.keysym == "0":
        data.mode = "splashScreen"
    if (data.mode == "splashScreen"): splashScreenKeyPressed(event, data)
    elif (data.mode == "survival"): survivalKeyPressed(event, data)
    elif (data.mode == "setUp"):      setUpKeyPressed(event, data)
    elif (data.mode == "war"):   warKeyPressed(event, data)
    elif (data.mode == "help"):       helpKeyPressed(event, data)
    elif (data.mode == "gameOver"):   gameOverKeyPressed(event, data)
    elif (data.mode == "about"):   aboutKeyPressed(event, data)
def timerFired(data):
    if (data.mode == "splashScreen"): splashScreenTimerFired(data)
    elif (data.mode == "survival"): survivalTimerFired(data)
    elif (data.mode == "setUp"):        setUpTimerFired(data)
    elif (data.mode == "war"):   warTimerFired(data)
    elif (data.mode == "help"):       helpTimerFired(data)
    elif (data.mode == "gameOver"):   gameOverTimerFired(data)
    elif (data.mode == "about"):   aboutTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): splashScreenRedrawAll(canvas, data)
    elif (data.mode == "survival"):    survivalRedrawAll(canvas, data)
    elif (data.mode == "setUp"):        setUpRedrawAll(canvas, data)
    elif (data.mode == "war"):   warRedrawAll(canvas, data)
    elif (data.mode == "help"):       helpRedrawAll(canvas, data)
    elif (data.mode == "gameOver"):   gameOverRedrawAll(canvas, data)
    elif (data.mode == "about"):   aboutRedrawAll(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    #root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1080, 720)