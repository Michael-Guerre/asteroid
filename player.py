from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y,num = 1, color = "white"):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.score = 0
        self.num = num
        self.color = color

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,self.color,self.triangle(),2)
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURNING_SPEED*dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.num == 1 :
            if keys[pygame.K_q]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_z]:
                self.move(dt)
            if keys[pygame.K_s]:
                self.move(-dt)
            if keys[pygame.K_SPACE]:
                self.shoot()
        else :
            if keys[pygame.K_LEFT]:
                self.rotate(-dt)
            if keys[pygame.K_RIGHT]:
                self.rotate(dt)
            if keys[pygame.K_UP]:
                self.move(dt)
            if keys[pygame.K_DOWN]:
                self.move(-dt)
            if keys[pygame.K_RCTRL]:
                self.shoot()
        self.shoot_timer-=dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer < 0:
            shot = Shot(self.position.x,self.position.y,self)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shoot_timer=0.3