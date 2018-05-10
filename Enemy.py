import math
from Unit import *

############## For math ##############
def crossProduct(a,b):
    # a(x1，y1) b(x2，y2) a×b=(x1y2-x2y1)
    return a[0]*b[1]-b[0]*a[1]
    

def segmentCross(P,Q):
    # [(x1,y1),(x2,y2)] 
    #  (Q1 - P1) ×  (Q2 - P1) <0
    # (P1 - Q1) × (P2 - P1) < 0
    Q2Q1 = (Q[1][0]-Q[0][0],Q[1][1]-Q[0][1])
    Q1P1 = (Q[0][0]-P[0][0],Q[0][1]-P[0][1])
    Q2P1 = (Q[1][0]-P[0][0],Q[1][1]-P[0][1])
    P1Q1 = (P[0][0]-Q[0][0],P[0][1]-Q[0][1])
    P2P1 = (P[1][0]-P[0][0],P[1][1]-P[0][1])
    d1 = crossProduct(P2P1,Q1P1)
    d2 = crossProduct(P2P1,Q2P1)
    d3 = crossProduct(Q2Q1,P1Q1)
    d4 = crossProduct(Q2Q1,P2P1)
    if d1*d2<0 and d3*d4 <0:
        return True
###############################

class Enemy(Unit):
    fullHealth = 100
    dirs= ["left","right","up","down"]
    def __init__(self,x,y,ImgList,attackList):
        super().__init__(x,y)    
        self.direction = 0
        self.speed = 2
        self.width = 64
        self.height = 80
        self.ImgList = ImgList
        self.attackList = attackList
        self.state = 0
        self.health = 100
        self.attack = 1
        self.direction = "left"
        self.attackInterval = 0
        self.free = 0
        self.blockAngle = None
    def draw(self,canvas,data):
        # Attacking
        if self.attackInterval>0:
            if self.direction in ["left","up"]:
                
                
                
                
                

                img = self.attackList[5-self.attackInterval]
                #img = self.ImgList[-2]
            if self.direction in ["right","down"]:
                img = self.attackList[10-self.attackInterval]
                #img = self.ImgList[-1]
                
        else:
            if self.direction == "left":
                start = 1
            elif self.direction == "right":
                start =2
            elif self.direction == "up":
                start=3
            elif self.direction == "down":
                start = 0
            img = self.ImgList[start*4+data.enemyMoveCount%4]                   
        canvas.create_image(self.x+data.scrollX,self.y+data.scrollY,image = img)  
        
        # Health 
        healthWidth = self.width
        healthHeight =self.height
        canvas.create_rectangle(self.x - healthWidth/2+data.scrollX,
                                self.y  - healthHeight/2 - 20+data.scrollY,
                               self.x + healthWidth/2+data.scrollX,
                                self.y- healthHeight/2 + 5- 20+data.scrollY,
                               fill = "white",width = 1)
        canvas.create_rectangle(self.x-healthWidth/2+data.scrollX,
                                self.y  - healthHeight/2- 20+data.scrollY,
                               self.x-healthWidth/2+2*healthWidth/2*self.health/Enemy.fullHealth+data.scrollX,
                               self.y- healthHeight/2 + 5- 20+data.scrollY,
                               fill = "tomato",width = 1)     
    ################
    
    def seePlayer(self,block,data):
        list = block.getFourNodes()
        relativeList = []
        P = [(self.x,self.y),(data.player.x-data.scrollX,data.player.y-data.scrollY)]
        # get relative position
        relativeList.append([list[0][0]-self.width/3,list[0][1]-self.height/2])
        relativeList.append([list[1][0]-self.width/3,list[1][1]+self.height/2])
        relativeList.append([list[2][0]+self.width/3,list[2][1]-self.height/2])
        relativeList.append([list[3][0]+self.width/3,list[3][1]+self.height/2])
        segmentA = [relativeList[0],relativeList[1]]
        segmentB = [relativeList[2],relativeList[3]]
        segmentC = [relativeList[0],relativeList[2]]
        segmentD = [relativeList[1],relativeList[3]]
        if segmentCross(P,segmentA) or segmentCross(P,segmentB) or segmentCross(P,segmentC) or segmentCross(P,segmentD):
            return False
        return True
    
    
    ################                       
    def move(self,player,data):
        
        deltaX = player.x-(self.x+data.scrollX)
        deltaY = player.y-(self.y+data.scrollY)
        
        for block in data.blocks:
            # Check if collision
            if self.checkBlock(block):
                self.free =1
                currentBlock = block
                self.blockAngle = self.findClosestSegment(block)
                break
            else:
                self.free =0
                self.blockAngle = None
                    
        if self.free ==1:
            # if collide but see player, leave collision
            if self.seePlayer(currentBlock,data):

                self.free =0
                self.blockAngle = None
                currentBlock = None
        if self.free ==0:
            #print("no collision")
            # Freely towards player
            angle = math.atan(deltaY / deltaX)
        
            dir = []
            if deltaY > 0:
                self.y+=abs(math.sin(angle)*self.speed)
                #self.direction = "down"
                dir.append("down")
            if deltaY<0:
                self.y-=abs(math.sin(angle)*self.speed)
                #self.direction = "up"
                dir.append("up")
            if deltaX > 0: # Enemy is at left side of player
                #self.direction = "right"
                dir.append("right")
                self.x+=abs(math.cos(angle)*self.speed)
            if deltaX<0:
                dir.append("left")
                self.x-=abs(math.cos(angle)*self.speed)
                #self.direction = "left"
            if abs(deltaX)>abs(deltaY):
                self.direction = dir[1]
            else:
                self.direction = dir[0]

                
        else:
            if self.blockAngle ==0:# Enemy is at left side of player
                self.direction = "right"
                self.x+=abs(math.cos(self.blockAngle)*self.speed)

            elif self.blockAngle ==math.pi/2:
                self.y-=abs(math.sin(self.blockAngle)*self.speed)
                self.direction = "up" 
            elif self.blockAngle ==math.pi:
                self.x-=abs(math.cos(self.blockAngle)*self.speed)
                self.direction = "left"
            elif self.blockAngle ==-math.pi/2:
                self.y+=abs(math.sin(self.blockAngle)*self.speed)
                self.direction = "down"

            
    def checkAttack(self,player,data):
        attackRange = 20
        deltaX = player.x-(self.x+data.scrollX)
        deltaY = player.y-(self.y+data.scrollY)
        if abs(deltaX)<=self.width and abs(deltaY) <= self.height/2:
            # AttackMode
            
            self.state = 1
            self.speed = 0
            
            if self.attackInterval == 0:
                self.attackInterval=5
                player.health -= self.attack
            
        else:
            self.state = 0
            self.speed = 2
        if self.attackInterval>0:
            self.attackInterval-=1   
            
            
#######################################################################################
# Check for block
########################################################################################            
    # free = 0
    def checkBlock(self,block):
        margin = 10
        if abs(self.x-block.x)<(block.width+self.width)/2 +margin and \
           abs(self.y-block.y)<(block.height + self.height)/2+ margin:
           # Collision!
           return True
            

    
    
    def disToSegment(self,a,b):
        #vector =    x    ,    y       
        apVec = (self.x-a[0],self.y-a[1])
        bpVec = (self.x-b[0],self.y-b[1])
        abVec = (b[0]-a[0],b[1]-a[1])
        r = (apVec[0] * abVec[0]+apVec[1] * abVec[1])/(abVec[0]**2+abVec[1]**2)
        # distance is ap
        if r<=0:
            distance = math.sqrt(apVec[0]**2 + apVec[1]**2)
        # distance is bp
        elif r>=1:
            distance = math.sqrt(bpVec[0]**2 + bpVec[1]**2)
        else:
            projection = (a[0]+abVec[0]*r,a[1]+abVec[1]*r)
            distance = math.sqrt((projection[0]-self.x)**2 +(projection[1]-self.y)**2)
        return distance        
            
    def findClosestSegment(self,block):
        # four nodes
        list = block.getFourNodes()
        relativeList = []
        # get relative position
        relativeList.append([list[0][0]-self.width/2,list[0][1]-self.height/2])
        relativeList.append([list[1][0]-self.width/2,list[1][1]+self.height/2])
        relativeList.append([list[2][0]+self.width/2,list[2][1]-self.height/2])
        relativeList.append([list[3][0]+self.width/2,list[3][1]+self.height/2])
        
        distance = []
        segmentA = [relativeList[0],relativeList[1]]
        distance.append(self.disToSegment(segmentA[0],segmentA[1]))
        segmentB = [relativeList[2],relativeList[3]]
        distance.append(self.disToSegment(segmentB[0],segmentB[1]))
        segmentC = [relativeList[0],relativeList[2]]
        distance.append(self.disToSegment(segmentC[0],segmentC[1]))
        segmentD = [relativeList[1],relativeList[3]]
        distance.append(self.disToSegment(segmentD[0],segmentD[1]))
        minIndex = distance.index(min(distance))
        segments = [segmentA,segmentB,segmentC,segmentD]
        cloestSeg = segments[minIndex]
        dX = cloestSeg[1][0]-cloestSeg[0][0]
        dY = cloestSeg[1][1]-cloestSeg[0][1]
        if minIndex==0:
            angle = -math.pi/2
        elif minIndex==1:
            angle = math.pi/2
        elif minIndex==2:
            angle = math.pi
        elif minIndex==3:
            angle = 0
        return angle