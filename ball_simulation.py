import pygame

pygame.init()
screen=pygame.display.set_mode((700,700))

box=pygame.Rect((100,100,500,500))
circle_radius=10
pos=[250,250]
velocity=[0,0]
acceleration=[0,0]
g=10
clock=pygame.time.Clock()

def collision_y():
    if pos[1] > box.bottom - circle_radius:
        pos[1] = box.bottom - circle_radius
        return True
    if pos[1] < box.top + circle_radius:
        pos[1] = box.top + circle_radius
        return True
    return False

def collision_x():
    if pos[0] > box.right - circle_radius:
        pos[0] = box.right - circle_radius
        return True
    if pos[0] < box.left + circle_radius:
        pos[0] = box.left + circle_radius
        return True
    return False

def physics(t):
    if collision_x():
        velocity[0]=-velocity[0]
    if collision_y():
        velocity[1]=-velocity[1]
    velocity[1]-=g*t
    velocity[0]+=acceleration[0]
    velocity[1]+=acceleration[1]
    pos[0]-=velocity[0]
    pos[1]-=velocity[1]

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    dt=clock.tick(60)/1000.0
    key=pygame.key.get_pressed()
    physics(dt)
    if key[pygame.K_UP]:
        acceleration[1]=0.5
    elif key[pygame.K_DOWN]:
        acceleration[1]=-0.5
    else:
        acceleration[1]=0
    if key[pygame.K_RIGHT]:
        acceleration[0]=-0.5
    elif key[pygame.K_LEFT]:
        acceleration[0]=0.5
    else:
        acceleration[0]=0
    
    if key[pygame.K_SPACE]:
        acceleration[0]=0
        acceleration[1]=0
        velocity[0]=0
        velocity[1]=0
    screen.fill((0,0,0))
    pygame.display.set_caption('[Arrow Keys] - Move    [SPACE] - Stop movement')
    pygame.draw.rect(screen,(64,64,64),box)
    pygame.draw.circle(screen,(255,255,255),(pos[0],pos[1]),circle_radius)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
