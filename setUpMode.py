####################################
# setUp mode
####################################

from Block import *


def setUpMousePressed(event, data):
    # Block can't collide each other nor can they collide with player start place
    if data.currentBlock!= None and\
     legal(event.x-data.scrollX,event.y-data.scrollY,data.currentBlock[0],data.currentBlock[1],data.blocks) and\
       legalPlayer(event.x-data.scrollX,event.y-data.scrollY,data,data.currentBlock[0],data.currentBlock[1]):
        data.blocks.add(Block(event.x-data.scrollX,event.y-data.scrollY,data.currentBlock[0],data.currentBlock[1],data.currentBlock[2]))
    else:
        
        for block in data.blocks:
            if block.x-block.width/2<event.x-data.scrollX<block.x+block.width/2 and\
            block.y-block.height/2<event.y-data.scrollY<block.y+block.height/2:
                data.chosenBlock = block
        
        
        
def setUpKeyPressed(event, data):
    if (event.keysym.lower() == 'h'):
        data.setUpHelp = 1-data.setUpHelp

    if event.keysym=="1":
        width = 150
        height=150
        data.currentBlock=[width,height,data.blockImg]
    elif event.keysym=="2":
        width = 150
        height=300
        data.currentBlock=[width,height,data.tallImg]
    elif event.keysym=="3":
        width = 300
        height=150
        data.currentBlock=[width,height,data.longImg]




    if event.keysym.lower() == "w" and data.scrollY<data.survivalHeight/2:
        data.scrollY +=15
    if event.keysym.lower() == "a" and data.scrollX<data.survivalWidth/2:
        data.scrollX +=15
    if event.keysym.lower() == "s" and data.scrollY>-data.survivalHeight/2:
        data.scrollY -=15
    if event.keysym.lower() == "d" and data.scrollX>-data.survivalWidth/2:
        data.scrollX -=15
    
    if event.keysym == "space":
        data.scrollX = 0
        data.scrollY = 0
        data.mode = "survival"
    if event.keysym == "BackSpace":
        if data.chosenBlock != None:
            data.blocks.remove(data.chosenBlock)
            data.chosenBlock = None
def setUpTimerFired(data):
    pass
    
def setUpRedrawAll(canvas, data):
    canvas.create_image(data.width/2+data.scrollX,data.height/2+data.scrollY ,image = data.edgeImg)
    canvas.create_image(data.width/2+data.scrollX,data.height/2+data.scrollY ,image = data.survivalBack)

    
    canvas.create_text(data.width/2, 90,
                       text="Press space to start", font="fixedsys 30")
    if data.currentBlock!= None:
        currentWid = data.currentBlock[0]
        currentHei = data.currentBlock[1]
        for block in data.blocks:
            left = block.x -64-(block.width+currentWid)/2
            top = block.y-100-(block.height+currentHei)/2
            right = block.x + 64+(block.width+currentWid)/2
            bottom = block.y + 100 + (block.height+currentHei)/2
            drawGrid(canvas,data,left,top,right,bottom)
    # Avoid player
        drawGrid(canvas,data,data.player.x-((64+currentWid)/2),data.player.y-((64+currentHei)/2),data.player.x+((64+currentWid)/2),data.player.y+((64+currentHei)/2))
    
    for block in data.blocks:
        block.draw(canvas,data)
        
    if data.chosenBlock != None:
        canvas.create_text(data.chosenBlock.x+data.scrollX,data.chosenBlock.y+data.scrollY,text="X",fill = "red",font="fixedsys 30")
        
    frameWid = data.setUpFrameImg.width()
    frameHei = data.setUpFrameImg.height()
    canvas.create_image(frameWid/2,data.height-frameHei/2 ,image = data.setUpFrameImg)
    if data.setUpHelp==1:
        canvas.create_image(data.width/2,data.height/2,image = data.setUpHelpImg)

#########
# Helper functions
#########
def legalPlayer(x,y,data,currentWid,currentHei):
    if (abs(data.player.x-x)<(64+currentWid)/2 and\
        abs(data.player.y-y)<(100+currentHei)/2):
        return False
    return True


def legal(x,y,currentWid,currentHei,blocks):
    for block in blocks:
        if insideBlock(x,y,currentWid,currentHei,block):return False
    return True

def insideBlock(x,y,currentWid,currentHei,block):
        if (abs(x-block.x)<(block.width+currentWid)/2 +64 and \
           abs(y-block.y)<(block.height +currentHei)/2 + 100):
               return True
        return False

def drawGrid(canvas,data,left,top,right,bottom):
    distance = 10
    for i in range(int((bottom-top)/distance)):
        topNew = top + i*distance
        BottomNew = topNew
        canvas.create_line(left+ data.scrollX,topNew+data.scrollY,right+data.scrollX,BottomNew+data.scrollY,fill = "coral",width = 2)
        canvas.create_rectangle(left+ data.scrollX,top+data.scrollY,right+data.scrollX,bottom+data.scrollY,fill = "",width = 2)

