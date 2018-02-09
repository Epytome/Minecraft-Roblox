import pygame
import random

# Initialize game engine
pygame.init()


#Images
roblox = pygame.image.load('Herobrine.png')
roblox = pygame.transform.scale(roblox, (400, 400))
robloxian = pygame.image.load('ghast.png')
robloxian = pygame.transform.scale(robloxian, (100, 100))
grass = pygame.image.load('MineGrass.png')
grass = pygame.transform.scale(grass, (800, 200))
owy = pygame.image.load('unnamed.png')
owy = pygame.transform.scale(owy, (40, 40))
house1 = pygame.image.load('MineHouse.png')
house1 = pygame.transform.scale(house1, (300, 90))
plank = pygame.image.load('Woodenplank.png')
plank = pygame.transform.scale(plank, (40, 40))
door = pygame.image.load('door.png')
door = pygame.transform.scale(door, (40, 80))
oak = pygame.image.load('oak.png')
oak = pygame.transform.scale(oak, (40, 40))
window = pygame.image.load('window.png')
window = pygame.transform.scale(window, (40, 40))
zombie = pygame.image.load('zombie.png')
zombie = pygame.transform.scale(zombie, (38, 80))
creeper = pygame.image.load('creeper.png')
creeper = pygame.transform.scale(creeper, (50, 80))
fence = pygame.image.load('fence.png')
fence = pygame.transform.scale(fence, (50, 80))
pumpkin = pygame.image.load('pumpkin.png')
pumpkin = pygame.transform.scale(pumpkin, (30, 30))
square1 = pygame.image.load('square.png')
square1 = pygame.transform.scale(square1, (36, 36))
square = pygame.image.load('square.png')
square = pygame.transform.scale(square, (42, 42))
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


# Block
col = [480, 460]
vel = [0, 0]
speed = 1

def draw_block(loc):
    x = loc[0]
    y = loc[1]
    
    screen.blit(creeper, (x,y))

#Sound Effects
thunder = pygame.mixer.Sound("sounds/Oofy.ogg")
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
num_flakes = 200
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
            if event.key == pygame.K_SPACE:
                vel[0] = 1
                vel[1] = 1 
            
            

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


    '''Creeper'''
    col[0] += vel[0]
    col[1] += vel[1]
    
    if  col[0] <= -10 or col[0] >= 760:
        vel[0] = -1 * vel[0]
            
    elif  col[1] <= 400 or col[1] >= 520:
        vel[1] = -1 * vel[1]


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
    screen.blit(grass, (0, 400))


    '''snowMAN'''

    if evil:
        snowman_eye = BLACK
    else:
        snowman_eye = RED

        
    screen.blit(pumpkin,(110, 430))
    screen.blit(square1,(107, 460))
    screen.blit(square,(104, 490))
    pygame.draw.ellipse(screen, BLACK, [124, 492, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [124, 500, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [124, 484, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [124, 476, 5, 5])
    pygame.draw.ellipse(screen, snowman_eye, [126, 435, 11, 11])
    pygame.draw.ellipse(screen, snowman_eye, [116, 435, 11, 11])

    if evil:
        snowman_eye = RED
    else:
        snowman_eye = BLACK




    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, BLACK, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, BLACK, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, BLACK, [0, 410], [800, 410], 5)




    '''Cweeper'''
    draw_block(col)

    '''Zombie'''
    screen.blit(zombie,(460, 320))





    ''' house '''
    screen.blit(oak,(420, 120))
    screen.blit(oak,(460, 160))
    screen.blit(oak,(420, 160))
    screen.blit(oak,(380, 160))
    screen.blit(oak,(500, 200))
    screen.blit(oak,(460, 200))
    screen.blit(oak,(420, 200))
    screen.blit(oak,(380, 200))
    screen.blit(oak,(340, 200))
    screen.blit(oak,(300, 200))
    screen.blit(oak,(540, 200))
    screen.blit(oak,(500, 160))
    screen.blit(oak,(460, 120))
    screen.blit(oak,(420, 80))
    screen.blit(oak,(380,120))
    screen.blit(oak,(340, 160))
    screen.blit(oak,(300, 200))
    screen.blit(plank,(300, 360))
    screen.blit(plank,(300, 320))
    screen.blit(plank,(300, 280))
    screen.blit(plank,(300, 240))
    screen.blit(plank,(340, 280))
    screen.blit(plank,(340, 240))
    screen.blit(plank,(380, 360))
    screen.blit(plank,(380, 320))
    screen.blit(plank,(380, 280))
    screen.blit(plank,(380, 240))
    screen.blit(plank,(420, 360))
    screen.blit(plank,(420, 320))
    screen.blit(plank,(420, 280))
    screen.blit(plank,(420, 240))
    screen.blit(plank,(460, 360))
    screen.blit(window,(460, 320))
    screen.blit(plank,(460, 280))
    screen.blit(plank,(460, 240))
    screen.blit(plank,(500, 360))
    screen.blit(plank,(500, 320))
    screen.blit(plank,(500, 280))
    screen.blit(plank,(500, 240))
    screen.blit(plank,(540, 360))
    screen.blit(plank,(540, 320))
    screen.blit(plank,(540, 280))
    screen.blit(plank,(540, 240))
    
    screen.blit(door,(340, 320))

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
