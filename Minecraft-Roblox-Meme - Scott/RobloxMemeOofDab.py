import pygame
import random

# Initialize game engine
pygame.init()


#Images
roblox = pygame.image.load('roblox.png')
robloxian = pygame.image.load('robloxian.png')
robloxian = pygame.transform.scale(robloxian, (100, 100))
logo = pygame.image.load('logo.png')
logo = pygame.transform.scale(logo, (800, 200))
owy = pygame.image.load('owy.png')
owy = pygame.transform.scale(owy, (40, 40))

# Window
width = 800
height = 600
SIZE = (width, height)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Lightning stuff
lightning_prob = 300 # (higher is less frequent)
lightning_timer = 0

#Sound Effects
thunder = pygame.mixer.Sound("sounds/roblox1.ogg")
pygame.mixer.music.load("sounds/minecraft.ogg")

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
BLACK = (0, 0, 0 )
WHITE2 = (210, 210, 210)
MAROON = (128, 0, 0)
GRAY = (150, 150, 150)
DARK_GRAY = (150, 150, 150)
NOT_QUITE_DARK_GRAY = (211, 211, 211)
RED = (255, 0 , 0)
ORANGE = (255, 128, 0)


#settings
sticky = True
ooof = True

''' make ground '''
ground = pygame.Surface([800, 200])
ground.fill(GREEN)

''' Make clouds '''
num_clouds = 30
near_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 100)
    loc = [x, y]
    near_clouds.append(loc)

num_clouds = 50
far_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 300)
    loc = [x, y]
    far_clouds.append(loc)

''' Make snow '''
num_flakes = 700
snow = []

for i in range(num_flakes):
    x = random.randrange(-100, 900)
    y = random.randrange(-100, 600)
    r = random.randrange(4, 7)
    stop = random.randrange(400, 625)
    flake = [x, y, r, r, stop]
    snow.append(flake)


lightning_timer = 0





def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    screen.blit(robloxian, (x,y))




def draw_snowflake(loc):
    x = loc[0]
    y = loc[1]
    screen.blit(owy, (x,y))

    
# Game loop

pygame.mixer.music.play(-1)

done = False
daytime = True
evil = True
spooky = True
scary = True

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            if event.key == pygame.K_BACKSPACE:
                evil = not evil
            if event.key == pygame.K_BACKSPACE:
                spooky = not spooky
            if event.key == pygame.K_BACKSPACE:
                scary = not scary
            
            

    # Game logic
    ''' move clouds '''
    for c in far_clouds:
        c[0] += 2

        if c[0] > 900:
            c[0] = random.randrange(-800, 0)
            c[1] = random.randrange(-50, 200)

    for c in near_clouds:
        c[0] += 2

        if c[0] > 900:
            c[0] = random.randrange(-800, 0)
            c[1] = random.randrange(-50, 200)

    ''' move rain '''

    if scary:
        scary_snow = WHITE
    else:
        scary_snow = RED

    
    for s in snow:
        s[0] += random.randrange(-1, 2)
        s[1] += random.randrange(1, 2)

        if s[1] >= s[4]:
            if sticky:
                pygame.draw.ellipse(ground, scary_snow, [s[0], s[1] - 402, s[3], s[3]])

            s[0] = random.randrange(-100, 900)
            s[1] = random.randrange(-100, 0)


    ''' flash lighting '''
    if ooof:
        if random.randrange(0, 50) == 0:
            lightning_timer = 5
            thunder.play()
        else:
            lightning_timer -= 1
            
    # Drawing code
    ''' sky '''
    if lightning_timer > 0:
        screen.blit(roblox, (200, 0))
    else:
        screen.fill(BLACK)


    ''' sun '''

    if spooky:
        spooky_sun = YELLOW
    else:
        spooky_sun = ORANGE

    pygame.draw.ellipse(screen, spooky_sun, [575, 75, 100, 100])


    ''' grass '''
    #pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    screen.blit(logo, (0, 400))


    '''snowMAN'''

    if evil:
        snowman_eye = BLACK
    else:
        snowman_eye = RED
    
    pygame.draw.ellipse(screen, WHITE2, [100 , 500, 60, 60])
    pygame.draw.ellipse(screen, WHITE2, [105, 460, 50, 50])
    pygame.draw.ellipse(screen, WHITE2, [110, 430, 40, 40])
    pygame.draw.ellipse(screen, BLACK, [126, 492, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [126, 500, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [126, 484, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [126, 476, 5, 5])
    pygame.draw.ellipse(screen, snowman_eye, [132, 445, 8, 8])
    pygame.draw.ellipse(screen, snowman_eye, [120, 445, 8, 8])

    if evil:
        snowman_eye = RED
    else:
        snowman_eye = BLACK


    ''' house '''
    pygame.draw.rect(screen, MAROON, [400, 300, 200, 100])
    pygame.draw.polygon(screen, WHITE2,[[380, 300], [500, 240], [620, 300]])
    pygame.draw.rect(screen, BLACK, [460, 320, 45, 80])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, BLACK, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, BLACK, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, BLACK, [0, 410], [800, 410], 5)



    ''' stars '''
    for s in snow:
        draw_snowflake(s)


    ''' clouds '''
    for c in near_clouds:
        draw_cloud(c)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
