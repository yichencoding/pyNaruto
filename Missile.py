
class Missile(object):
    def __init__(self,x, y,dir,attack):
        self.x = x
        self.y = y

        self.speed = 30
        self.size = 10
        self.dir=dir
        self.attack = attack
        
    def draw(self, canvas, data):
        canvas.create_image(self.x,self.y,image = data.missileImg)
    
    def move(self):
        self.x+=self.dir*self.speed
    def hitEnemy(self,enemy):
        deltaX = abs(enemy.x-self.x)
        if deltaX < 20:
            enemy.health-=self.attack
            return True
            