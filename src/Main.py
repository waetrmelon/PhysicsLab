import pygame
import Objects
import GUI
import MathUtil

background_colour = (40,43,48)
(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('PhysicsLab')
screen.fill(background_colour)

running = True
clock = pygame.time.Clock()
SceneObjects = [Objects.Circle(500,50,100)]

# Physics Settings
Step = (0.01) * 1
RenderHUD = False
FPS = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            SceneObjects.append(Objects.Circle(pos[0], pos[1], 100))
    dt = clock.tick(FPS)/1000
    screen.fill(background_colour)

    for Object1 in SceneObjects:
        Object1.Update(screen,dt+Step)

    if RenderHUD: GUI.RenderHUD(screen, clock)
    pygame.display.update()