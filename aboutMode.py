####################################
# about mode
####################################

def aboutMousePressed(event, data):
    pass

def aboutKeyPressed(event, data):
    data.mode ="splashScreen"
    
def aboutTimerFired(data):
    pass
    
def aboutRedrawAll(canvas, data):
    canvas.create_image(data.width/2,data.height/2,image= data.aboutImg)