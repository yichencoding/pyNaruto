def drawSurvivalFrame(canvas,data):
    margin = 20
    widthMargin = 50
    blockSize = 120
    if data.player.gun!= None:
        canvas.create_image(widthMargin+blockSize/2 +(blockSize+margin )* 0,margin/2 +data.lineHeight + blockSize/2 ,image =data.weaponImg)
        
        
    
    # Player status
    canvas.create_text(margin,150,text ="Lvl: "+str(data.player.level) ,font="fixedsys 26 bold",anchor = "w")
    
    attackWidth = data.attackStatus0Img.width()
    attackHeight = data.attackStatus0Img.height()
    if data.player.level ==0:
        attackImg = data.attackStatus0Img
    elif data.player.level ==1:
        attackImg = data.attackStatus1Img
    elif data.player.level ==2:
        attackImg = data.attackStatus2Img
    elif data.player.level >=3:
        attackImg = data.attackStatus3Img
    canvas.create_image(attackWidth/2,data.height-attackHeight/2,image =attackImg)
    canvas.create_rectangle(0,72,140*(data.player.health/100),90,fill = "tomato")
    canvas.create_rectangle(0,91,140*(data.player.magic/100),106,fill = "blue")
    canvas.create_rectangle(0,106,140*(data.player.exp/120),120,fill = "green")
    # Time
    canvas.create_text(data.width/2,margin,text ="Time: "+str(data.timeCounter/1000) +"s",font="fixedsys 26 bold")

    

                      