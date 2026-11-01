import pygame
pygame.init()
width=1900
height=600
screen=pygame.display.set_mode((width,height))
run=True
player=pygame.image.load('player_walk_right1.png').convert()
player=pygame.transform.scale(player,(100,200))
player_x=10
player_x_no_move=1795
sky_land=pygame.image.load('sky_land.png').convert()
sky_land=pygame.transform.scale(sky_land,(400,400))
sky_land.set_colorkey((0,0,0))
oject_x=0
duty=-1
duty_box=pygame.image.load('nothing.png').convert_alpha()
duty_box=pygame.transform.scale(duty_box,(400,400))

def player_move_right(player,player_x,key,player_x_no_move,oject_x):
    if key[pygame.K_j]:#dư
        if player_x<=1395:
            player_x+=1
            if player_x%2==0:
                player=pygame.image.load('player_walk_right1.png').convert_alpha()
                player=pygame.transform.scale(player,(100,200))
            else:
                player=pygame.image.load('player_walk_right2.png').convert_alpha()
                player=pygame.transform.scale(player,(100,200))
        else:
            player_x_no_move+=1
            if player_x_no_move%2==0:
                player=pygame.image.load('player_walk_right1.png').convert_alpha()
                player=pygame.transform.scale(player,(100,200))
                oject_x-=1
            else:
                player=pygame.image.load('player_walk_right2.png').convert_alpha()
                player=pygame.transform.scale(player,(100,200))
                oject_x-=1
    return player,player_x,player_x_no_move,oject_x



def player_move_left(player,player_x,key,player_x_no_move,oject_x):
    if player_x>=10:
        player_x-=1
        if player_x%2==0:
            player=pygame.image.load('player_walk_left1.png').convert_alpha()
            player=pygame.transform.scale(player,(100,200))
        else:
            player=pygame.image.load('player_walk_left2.png').convert_alpha()
            player=pygame.transform.scale(player,(100,200))
    else:
        player_x_no_move-=1
        if player_x_no_move%2==0:
            player=pygame.image.load('player_walk_left1.png').convert_alpha()
            player=pygame.transform.scale(player,(100,200))
            oject_x+=1
        else:
            player=pygame.image.load('player_walk_left2.png').convert_alpha()
            player=pygame.transform.scale(player,(100,200))
            oject_x+=1
    return player,player_x,player_x_no_move,oject_x


def get_duty(NPC_x,player_x,duty):
    if key[pygame.K_q] and (NPC_x-player_x<=30 or player_x-NPC_x<=30):
        q_pressed=False
        if not q_pressed:
            if duty==0:
                print(9)
            elif duty==1:
                print(0)
        q_pressed=True
    return NPC_x,player_x,duty

    
q_pressed = False
while run:
    key=pygame.key.get_pressed()
    screen.fill((0,0,0))
    
    if key[pygame.K_j]:#từ đoạn dưới
        player,player_x,player_x_no_move,oject_x=player_move_right(player,player_x,key,player_x_no_move,oject_x)
    elif key[pygame.K_f]:
        player,player_x,player_x_no_move,oject_x=player_move_left(player,player_x,key,player_x_no_move,oject_x)
    NPC_x=180+oject_x
    screen.blit(sky_land,(180 + oject_x,200))
    player.set_colorkey((0,0,0))
    screen.blit(player,(player_x,200))
#hết đoạn dchuyen

#bị lỗi
    if key[pygame.K_q]:
        if not q_pressed:
            if abs(NPC_x - player_x) <= 100:
                duty += 1
            q_pressed = True
    else:
        q_pressed = False
    if duty == 0:
        duty_box = pygame.image.load('duty_box1.png').convert_alpha()
        duty_box = pygame.transform.scale(duty_box, (100, 200))
    elif duty == 1:
        duty_box = pygame.image.load('duty_box2.png').convert_alpha()
        duty_box = pygame.transform.scale(duty_box, (100, 200))
    if duty >= 0:
        screen.blit(duty_box, (0, 100))
    
#phần này nó không hiện hộp thoại cô ơi

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
