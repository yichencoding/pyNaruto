####################################
# splashScreen mode
####################################

def splashScreenMousePressed(event, data):
    # Play
    if data.playX-data.blockWid/2<event.x<data.playX+data.blockWid/2 and \
        data.playY-data.blockHei/2<event.y<data.playY + data.blockHei/2:
        data.mode = "setUp"
    # Help
    if data.helpX-data.blockWid/2<event.x<data.helpX+data.blockWid/2 and \
        data.helpY-data.blockHei/2<event.y<data.helpY + data.blockHei/2:
        data.prevMode = data.mode    
        data.mode = "help"
    # About
    if data.aboutX-data.blockWid/2<event.x<data.aboutX+data.blockWid/2 and \
        data.aboutY-data.blockHei/2<event.y<data.aboutY + data.blockHei/2:
        #data.prevMode = data.mode   
        data.mode = "about"

def splashScreenKeyPressed(event, data):
    #data.mode = "survival"
    pass

def splashScreenTimerFired(data):
    pass

def splashScreenRedrawAll(canvas, data):
    canvas.create_image(data.width/2,data.height/2,image = data.splashBackImg)
    canvas.create_text(data.width/2, 50,
                       text="TINY GAME", font="fixedsys 35 bold")
    #canvas.create_text(data.width/2, data.height/2+20,
    #                   text="Press any key to play!", font="Arial 20")
                       
                       
                            
    canvas.create_image(data.playX,data.playY,image =    data.menuBlockImg)                
                           
    canvas.create_text(data.playX, data.playY,
                       text="PLAY", font="fixedsys 28")
                            
    
    canvas.create_image(data.helpX,data.helpY,image =    data.menuBlockImg)
    canvas.create_text(data.helpX, data.helpY,
                       text="HELP", font="fixedsys 28")
                       
    canvas.create_image(data.aboutX,data.aboutY,image =    data.menuBlockImg)
    canvas.create_text(data.aboutX, data.aboutY,
                       text="ABOUT", font="fixedsys 28")
    