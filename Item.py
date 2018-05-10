class Item(object):
    def __init__(self,x,y,attack,img):
        self.x = x
        self.y = y
        self.attack = attack
        self.state = 0
        self.ammo = 20
        self.image = img
        self.collection = 0
        
        
    def draw(self,canvas,data):
        canvas.create_image(self.x + data.scrollX,
                            self.y + data.scrollY,image = self.image)