
#from tkinter import *
#from Soldier import *


def calculateMoney(data):
        data.money+=data.moneyspeed
        
def drawWarFrame(canvas,data):
    margin = 20
    # Each element                    
    canvas.create_image(data.width/2,(data.height-data.lineHeight)/2+data.lineHeight,image = data.frameBack)  
    # Draw money ...
    canvas.create_text(margin,margin,text="Money: "+str(data.money ), anchor="w",
                    fill="black", font="fixedsys 28 bold ")
    
    widthMargin = 20
    blockSize = 140
    for i in range(5):
        canvas.create_image(widthMargin+blockSize/2 +(blockSize+margin )* i,margin/2 +data.lineHeight + blockSize/2 ,image =data.frameBlockImg)
        canvas.create_image(widthMargin+blockSize/2 +(blockSize+margin )* i,margin/2 +data.lineHeight + blockSize/2 ,image =data.headsImg[i])   
        
    #if data.player.gun!= None:
    #    canvas.create_image(widthMargin+blockSize/2 +(blockSize+margin )* 0,margin/2 +data.lineHeight + blockSize/2 ,image =data.weaponImg)