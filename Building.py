#from tkinter import *


class Building(object):
    health = 10000
    award = 500
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.health = 10000
        self.size = 50
        # no attack
        self.state = 0
        self.img = img
    
    def draw(self,canvas,data):
        margin = 10
        healthHei = 20
        imgWidth = data.baseImg.width()
        imgHeight = data.baseImg.height()
        canvas.create_image(self.x,self.y,image = self.img)
        # Health                        
        canvas.create_rectangle(self.x-self.size,self.y-self.size-healthHei,
                               self.x+self.size,self.y-self.size-healthHei+margin,
                               fill = "white",width = 1)
        canvas.create_rectangle(self.x-self.size,self.y-self.size-healthHei,
                               self.x-self.size+2*self.size*self.health/Building.health,
                               self.y-self.size-healthHei+margin,
                               fill = "green",width = 1)      
                               
                               
def removeBuilding(set):
    for element in set:
        print(element.health)
        if element.health<=0:
            set.remove(element)
            break