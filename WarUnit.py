class WarUnit(object):
    cost = 100
    def __init__(self,dir,x,y,speed,range,imgList,attackList,cost):
        self.health = 100
        self.attack = 10
        # state = 0 means walk
        # State = 1 attack
        self.state = 0
        self.cost = 0
        
        self.width = 64
        self.height = 100
        self.dir = dir
        self.x = x
        self.y = y
        self.speed = speed
        self.range = range
        self.imgList = imgList
        self.attackList = attackList
        self.cost = cost
        self.attackInterval=0

    def move(self):
        self.x += self.dir * self.speed   
        
    def draw(self,canvas,data):
        if self.attackInterval>0:
            
            
            if self.dir ==-1:
                img = self.attackList[5-self.attackInterval]
                color = "red"
            if self.dir ==1:
                color = "green"
                img = self.attackList[10-self.attackInterval]
        
        
        
        
        else:
            if self.dir ==1:# Moving right
                img = self.imgList[2*4+data.enemyMoveCount%4]
                color = "green"
            else:
                img = self.imgList[1*4+data.enemyMoveCount%4]
                color = "red"
                
        canvas.create_image(self.x,self.y,image = img)
        canvas.create_rectangle(self.x-self.width/2,
                                self.y  - 50/2- 20,
                               self.x-self.width/2+2*self.width/2*self.health/100,
                               self.y- 50/2 + 5- 20,
                               fill = color,width = 1)
        
    def getDisBetweenObj(self,other):
        deltaX = other.x-self.x
        deltaY = other.y-self.y
        return abs(deltaX)
        
        
    def checkHit(self,other):
        
        if other != None and self.getDisBetweenObj(other) < self.range:
            self.state =1
            if self.attackInterval==0:
                self.attackInterval=5
                
                other.health-=self.attack
            # can only attack one once
             
            return True
            
        else:
            self.state = 0
