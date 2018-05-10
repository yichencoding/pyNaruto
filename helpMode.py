####################################
# help mode
####################################
def helpMousePressed(event, data):
    pass

def helpKeyPressed(event, data):
    if event.keysym == "Left" and data.page >0:
        data.page -=1
    if event.keysym == "Right" and data.page <2:
        data.page +=1
    elif event.keysym != "Left" and event.keysym != "Right" :
        data.mode = data.prevMode
        data.page = 0
    

def helpTimerFired(data):
    pass

def helpRedrawAll(canvas, data):
    canvas.create_image(data.width/2,data.height/2,image = data.helpImg)
    if data.page == 0:
        
        canvas.create_image(data.width/2,data.height/2,image = data.setUpHelpImg)
    if data.page == 1:
        canvas.create_image(data.width/2,data.height/2,image = data.survivalHelpImg)
    if data.page == 2:
        canvas.create_image(data.width/2,data.height/2,image = data.warHelpImg)