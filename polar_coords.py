import pygame # type: ignore
import pygame.gfxdraw 
import numpy as np # type : ignore

# starting the pygame and stuff
pygame.init()
WIDTH = 720
HEIGHT = WIDTH
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # window size config
pygame.display.set_caption("Polar Coords") # caption of the window
clock = pygame.time.Clock() # init the clock system
my_font = pygame.font.SysFont('Arial', 30) # init a font

# main loop
running = True

def polar_func(theta):
    return np.sin(theta)

t = 150

while running:
    # loop in every event
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if quit button pressed, stop running
            running = False   

    screen.fill((0,0,0)) # fill the screen with black color
    #
    
    points = []

    k = 10*pygame.mouse.get_pos()[0]/WIDTH
    for i in range(t):
        theta = 2*np.pi*i/t
        r = polar_func(k * theta)*200

        x = r*np.cos(theta)
        y = r*np.sin(theta)
        points.append((x + WIDTH*0.5,y + HEIGHT*0.5))

    pygame.gfxdraw.aapolygon(screen, points, (255,255,255))

    text_surface = my_font.render(f"k factor = {k:.5f}", True, (255, 255, 255))
    screen.blit(text_surface, (50, 50))

    #
    pygame.draw.line(screen, (255,0,0), (WIDTH*0.5,0), (WIDTH*0.5,HEIGHT)) # y axis
    pygame.draw.line(screen, (0,255,0), (0,HEIGHT*0.5), (WIDTH,HEIGHT*0.5)) # x axis

    pygame.display.flip() # render 
    clock.tick(10) # set the fps

pygame.quit() #quit the pygame