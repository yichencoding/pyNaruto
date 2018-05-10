import math
class Bullet(object):
    def __init__(self,x, y,dx,dy,direction,attack):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.speed = 50
        self.size = 10
        self.direction = direction
        self.attack = attack
        
    def draw(self, canvas, data):
        
        canvas.create_image  (self.x+data.scrollX,
                               self.y +data.scrollY,
                               image = data.bulletImg)
    
    def move(self):
        self.x+=math.cos(self.direction)*self.dx*self.speed
        self.y+=math.sin(self.direction)*self.dy*self.speed

    def hitEnemy(self,enemy):
        deltaX = enemy.x-self.x
        deltaY = enemy.y-self.y
        dis = deltaX **2 + deltaY **2
        if dis < enemy.width **2:
            enemy.health-=self.attack
            return True
            