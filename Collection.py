from Item import *
class Collection(Item):
    def __init__(self,x,y,sx,sy,img):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.image = img
        self.collected = 0
        
        
        
    def draw(self,canvas,data):
        if self.collected ==0:
            
            canvas.create_image(self.x + data.scrollX,
                            self.y + data.scrollY,image = self.image)