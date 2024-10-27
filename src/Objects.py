import pygame
import Constants

class Circle():
    def __init__(self,x,y,mass) -> None:

        self.Position = pygame.Vector2()
        self.Position.x = x
        self.Position.y = y

        self.Velocity = pygame.Vector2()
        self.Force =  pygame.Vector2()

        self.Mass = mass

    def Update(self,screen, dt):

        self.Render(screen)

        self.Force += self.Mass * pygame.Vector2(0,Constants.GRAVITY)
        self.ApplyContraints()
        self.Velocity += self.Force / self.Mass * dt
        self.Velocity.y *= 0.999
        self.Position += self.Velocity * dt
        self.Force = pygame.Vector2(0,0)

    def Render(self,screen):
        pygame.draw.circle(screen, (255,0,0), (self.Position.x, self.Position.y), 5)

    def ApplyContraints(self):
        if self.Position.y > 720:
            self.Velocity.y *= -1
        if self.Position.y < 0:
            self.Velocity.y *= -1

        if self.Position.x < 0:
            self.Velocity.x *= -1
        if self.Position.x > 1280:
            self.Velocity.x *= -1