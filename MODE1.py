import pygame
import random
pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('test')
#background chính
sky=pygame.image.load('sky.jpg').convert()
sky=pygame.transform.scale(sky,(SCREEN_WIDTH,SCREEN_HEIGHT))
way1=pygame.image.load('way.png').convert_alpha()
way1=pygame.transform.scale(way1,(SCREEN_WIDTH,SCREEN_HEIGHT))
way2=pygame.image.load('way.png').convert_alpha()
way2=pygame.transform.scale(way2,(SCREEN_WIDTH,SCREEN_HEIGHT))
way3=pygame.image.load('way.png').convert_alpha()
way3=pygame.transform.scale(way3,(SCREEN_WIDTH,SCREEN_HEIGHT))
way4=pygame.image.load('way.png').convert_alpha()
way4=pygame.transform.scale(way4,(SCREEN_WIDTH,SCREEN_HEIGHT))
#chuyển chế độ - home
home1=pygame.image.load('home1.png').convert_alpha()
home1.set_colorkey((0,0,0))
home1=pygame.transform.scale(home1,(SCREEN_WIDTH,SCREEN_HEIGHT))
home2=pygame.image.load('home2.png').convert_alpha()
home2.set_colorkey((0,0,0))
home2=pygame.transform.scale(home2,(SCREEN_WIDTH,SCREEN_HEIGHT))
#cảnh vật phụ
sky_land=pygame.image.load('land_sky.png').convert_alpha()
sky_land.set_colorkey((0,0,0))
sky_land=pygame.transform.scale(sky_land,(800,500))
tree=pygame.image.load('tree.png').convert_alpha()
tree.set_colorkey((0,0,0))
tree=pygame.transform.scale(tree,(SCREEN_WIDTH*1.2,SCREEN_HEIGHT-100))
oject_x=0
#hướng dẫn
note1=pygame.image.load('note1.png').convert_alpha()
note1.set_colorkey((0,0,0))
note1=pygame.transform.scale(note1,(250,150))
note2=pygame.image.load('note2.png').convert_alpha()
note2.set_colorkey((0,0,0))
note2=pygame.transform.scale(note2,(250,150))
note3=pygame.image.load('note3.png').convert_alpha()
note3.set_colorkey((0,0,0))
note3=pygame.transform.scale(note3,(SCREEN_WIDTH-800,SCREEN_HEIGHT-300))
#NPC
NPC=pygame.image.load('NPC.png').convert_alpha()
NPC=pygame.transform.scale(NPC,(450,550))
NPC.set_colorkey((0,0,0))
stopper=pygame.image.load('stopper.png').convert_alpha()
stopper=pygame.transform.scale(stopper,(400,300))
#player-người chơi
player=pygame.image.load('player_walk_right1.png').convert_alpha()
player=pygame.transform.scale(player,(100,175))
player.set_colorkey((0,0,0))
player_x=600
player_x_no_move=1395
#nhiệm vụ
duty=-1
duty_box=pygame.image.load('nothing.png').convert_alpha()
duty_box=pygame.transform.scale(duty_box,(400,400))
#câu hỏi nhiệm vụ
answer_true=[pygame.image.load('answer_true.jpg').convert_alpha(),True]#đáp án đúng
answer_true[0]=pygame.transform.scale(answer_true[0],(400,200))
answer_true[0].set_colorkey((0,0,0))
answer_false1=[pygame.image.load('answer_false1.jpg').convert_alpha(),False]#đ.án sai
answer_false1[0]=pygame.transform.scale(answer_false1[0],(400,200))
answer_false1[0].set_colorkey((0,0,0))
answer_false2=[pygame.image.load('answer_false2.jpg').convert_alpha(),False]#đ.án sai
answer_false2[0]=pygame.transform.scale(answer_false2[0],(400,200))
answer_false2[0].set_colorkey((0,0,0))
answer_false3=[pygame.image.load('answer_false3.jpg').convert_alpha(),False]#đ.án sai
answer_false3[0]=pygame.transform.scale(answer_false3[0],(400,200))
answer_false3[0].set_colorkey((0,0,0))
answer_list=[answer_true,answer_false1,answer_false2,answer_false3]#ds đ.án
answer=-1
choose=None
#kết quả nv
wrong=(pygame.image.load('wrong1.png').convert())
wrong = pygame.transform.scale(wrong, (SCREEN_WIDTH,SCREEN_HEIGHT))
wrong.set_colorkey((0,0,0))
def player_move_right(player,player_x,key,player_x_no_move,oject_x,stopper_x):
    if key[pygame.K_j]:#dư
        if player_x<=1295:
            player_x+=1
            if player_x%2==0:
                player=pygame.image.load('player_walk_right1.png').convert_alpha()
                player=pygame.transform.scale(player,(100,175))
            else:
                player=pygame.image.load('player_walk_right2.png').convert_alpha()
                player=pygame.transform.scale(player,(100,175))
        else:
            if not (player_x==stopper_x+200):
                player_x_no_move+=1
                if player_x_no_move%2==0:
                    player=pygame.image.load('player_walk_right1.png').convert_alpha()
                    player=pygame.transform.scale(player,(100,175))
                    oject_x-=1
                else:
                    player=pygame.image.load('player_walk_right2.png').convert_alpha()
                    player=pygame.transform.scale(player,(100,175))
                    oject_x-=1
            

    return player,player_x,player_x_no_move,oject_x,stopper_x



def player_move_left(player,player_x,key,player_x_no_move,oject_x,home_x):
    if player_x>=0:
        player_x-=1
        if player_x%2==0:
            player=pygame.image.load('player_walk_left1.png').convert_alpha()
            player=pygame.transform.scale(player,(100,175))
        else:
            player=pygame.image.load('player_walk_left2.png').convert_alpha()
            player=pygame.transform.scale(player,(100,175))
    else:
        if not (player_x<=home_x):
            player_x_no_move-=1
            if player_x_no_move%2==0:
                player=pygame.image.load('player_walk_left1.png').convert_alpha()
                player=pygame.transform.scale(player,(100,175))
                oject_x+=1
            else:
                player=pygame.image.load('player_walk_left2.png').convert_alpha()
                player=pygame.transform.scale(player,(100,175))
                oject_x+=1
        
    return player,player_x,player_x_no_move,oject_x,home_x


def sort_answer(answer_true,answer_false1,answer_false2,answer_false3):
    answer_list=[answer_true,answer_false1,answer_false2,answer_false3]
    ordered_list=[]
    choices=list(answer_list)
    while choices:
        next_choice=random.choice(choices)
        ordered_list.append(next_choice)
        choices.remove(next_choice)
    return ordered_list


def answer_apear(oder_answer_list):
    screen.blit(oder_answer_list[0][0],(300,75))
    screen.blit(oder_answer_list[1][0],(900,75))
    screen.blit(oder_answer_list[2][0],(300,325))
    screen.blit(oder_answer_list[3][0],(900,325))


def choose_answer1(oder_answer_list,choose,answer,mouse_pos):
    positions=[(300, 75),(900, 75),(300, 325),(900, 325)]
    for index, option in enumerate(oder_answer_list):
        rect = option[0].get_rect(topleft=positions[index])
        if rect.collidepoint(mouse_pos):
            choose = option
            return 0 if option[1] else 1
    return answer


def choose_answer2(answer,wrong,duty):
    if answer==0:
        duty+=2
    elif answer==1:
        screen.blit(wrong,(0,0))
    return duty

#main programe
run=True
oder_answer_list=sort_answer(answer_true,answer_false1,answer_false2,answer_false3)
#DIEU CHINH
q_pressed = False
while run:
    NPC_x=oject_x+2000
    stopper_x=oject_x+2500
    home_x=oject_x
    key=pygame.key.get_pressed()
    screen.fill((0,0,0))
    #hiển thị
    screen.blit(sky,(0,0))
    screen.blit(sky_land,(300 + oject_x,100))
    
    screen.blit(way1,(oject_x,0))
    screen.blit(way2,(oject_x+1500,0))
    screen.blit(tree,(500 + oject_x,0))
    screen.blit(note2,(1800 + oject_x,550))
    
    screen.blit(NPC,(NPC_x,200))
    screen.blit(stopper,(stopper_x,435))
    screen.blit(home1,(oject_x,0))
    screen.blit(note1,(150 + oject_x,550))
    

    if key[pygame.K_j]:
        player,player_x,
        player,player_x,player_x_no_move,oject_x,stopper_x=player_move_right(player,player_x,key,player_x_no_move,oject_x,stopper_x)
        
    
    elif key[pygame.K_f]:
        player,player_x,player_x_no_move,oject_x,home_x=player_move_left(player,player_x,key,player_x_no_move,oject_x,home_x)
    screen.blit(player,(player_x,535))
    screen.blit(home2,(oject_x,0))
    screen.blit(way3,(oject_x,20))
    screen.blit(way4,(oject_x+1500,20))

        


#phần nhiệm vụ
    if key[pygame.K_q]:
        if not q_pressed:
            if abs(NPC_x - player_x) <= 400:
                duty += 1
            q_pressed = True
    else:
        q_pressed = False
    if duty == 0:
        duty_box = pygame.image.load('duty_box1.jpg').convert_alpha()
        duty_box = pygame.transform.scale(duty_box, (SCREEN_WIDTH,SCREEN_HEIGHT-200))
        duty_box.set_colorkey((0,0,0))
    elif duty == 1:
        duty_box = pygame.image.load('duty_box2.jpg').convert_alpha()
        duty_box = pygame.transform.scale(duty_box, (SCREEN_WIDTH,SCREEN_HEIGHT-200))
        duty_box.set_colorkey((0,0,0))
    elif duty==2:
        #DIEU CHINH
        answer_apear(oder_answer_list)
        screen.blit(note3,(460,100))
        duty=choose_answer2(answer, wrong,duty)

        #answer=choose_answer1(oder_answer_list,choose,answer)
        #answer_apear(oder_answer_list)
        #for event in pygame.event.get():
            #if event.type==pygame.MOUSEBUTTONDOWN:
                #answer=choose_answer1(oder_answer_list,choose,answer)
        #choose_answer2(answer,congratulation,wrong)
    elif duty==3:
            duty=2
    elif duty == 4:
        duty_box = pygame.image.load('duty_box3.jpg').convert_alpha()
        duty_box = pygame.transform.scale(duty_box, (SCREEN_WIDTH,SCREEN_HEIGHT-200))
        duty_box.set_colorkey((0,0,0))
    elif duty == 5:
        duty_box = pygame.image.load('duty_box4.jpg').convert_alpha()
        duty_box = pygame.transform.scale(duty_box, (SCREEN_WIDTH,SCREEN_HEIGHT-200))
        duty_box.set_colorkey((0,0,0))

    if duty >= 0:
        if duty<=5:
            screen.blit(duty_box, (0, 200))
    
    #DIEU CHINH
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and duty == 2:
            answer = choose_answer1(oder_answer_list, choose, answer, event.pos)
    
    #for event in pygame.event.get():
        #if event.type==pygame.QUIT:
            #run=False
        
        
    pygame.display.flip()
pygame.quit()
