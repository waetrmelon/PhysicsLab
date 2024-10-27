import pygame
pygame.font.init()
Font = pygame.font.SysFont('Arial', 30)

def RenderHUD(screen, clock):
    text_surface = Font.render('FPS: {}'.format(int(clock.get_fps())), False, (255, 255, 255))
    screen.blit(text_surface, (0,0))