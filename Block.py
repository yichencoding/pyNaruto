class Block(object):
    def __init__(self,x,y,width,height,image=None):
        self.x= x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        
    def draw(self,canvas,data):                     
        canvas.create_image(self.x+data.scrollX,  self.y+data.scrollY     ,image = self.image)                 
                                
                                
    def getFourNodes(self):
        list = []
        for x in [self.x-self.width/2,self.x+self.width/2]:
            for y in [self.y-self.height/2,self.y+self.height/2]:
                p = (x,y)
                list.append(p)
                
        return list