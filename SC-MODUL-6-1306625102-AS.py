import pygame, sys
from pygame.locals import *

def GambarBackground():
    layar.fill(green)
    # garis lantai di dasar layar
    pygame.draw.line(layar, black, (0, y_lantai), (lebar, y_lantai), 10)
    layar.blit(text1, [355, 5])                      # tulisan background

def GerakanBolaJatuh(bOXX, bOYY):
    vb0 = 10     # 10 pixel/clock  ke bawah
    GB = True    # GB =  gerak bola

    while GB == True:
        pygame.event.pump()          # supaya jendela tidak macet
        SbOY = vb0                   # lintasan bola-0
        bOYY = bOYY + SbOY           # posisi bola-0

        if bOYY >= y_lantai - 25:    # bola sampai di atas garis lantai
            bOYY = y_lantai - 25
            GB = False               # bola berhenti

        GambarBackground()
        #GambarBola
        pygame.draw.circle(layar, white, [bOXX, bOYY], 20)
        pygame.display.flip()
        fpsClock.tick(fps)
    return bOXX, bOYY


# Initialize Pygame
pygame.init()

# Define some colors
white = (250, 250, 250);   whitdull = (243, 243, 242)
black = (70, 70, 70);      green = (0, 176, 80)

# ukuran layar dan posisi garis lantai
lebar, tinggi = 1050, 650
y_lantai = tinggi - 15           # garis berada di dasar layar

layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Simulasi Bola Jatuh Bebas")
font1 = pygame.font.SysFont("arial", 30)
text1 = font1.render("Simulasi Bola Jatuh Bebas", True, white)
bOX, bOY = 525, 50                 # posisi awal bola

fps = 20
fpsClock = pygame.time.Clock()

# program utama Pygame
done = False
while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            bOY = 50                                   # bola kembali ke atas
            bOX, bOY = GerakanBolaJatuh(bOX, bOY)

    GambarBackground()
    pygame.draw.circle(layar, white, [bOX, bOY], 20)   #Gambar Bola posisi awal

    #Tampilkan semua gambar di layar
    pygame.display.flip()

    # Get the current mouse position (x,y)
    player_position = pygame.mouse.get_pos()
    xm = player_position[0]
    ym = player_position[1]

#end program
pygame.quit()