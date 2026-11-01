import asyncio
import pygame
import random

async def main():
    pygame.init()
    clock=pygame.time.Clock()
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
    note4=pygame.image.load('note4.png').convert_alpha()
    note4.set_colorkey((0,0,0))
    note4=pygame.transform.scale(note4,(250,150))
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
#đánh dấu câu hỏi
    A=(pygame.image.load('A.png').convert())
    A = pygame.transform.scale(A, (100,100))
    A.set_colorkey((0,0,0))
    B=(pygame.image.load('B.png').convert())
    B = pygame.transform.scale(B, (100,100))
    B.set_colorkey((0,0,0))
    C=(pygame.image.load('C.png').convert())
    C = pygame.transform.scale(C, (100,100))
    C.set_colorkey((0,0,0))
    D=(pygame.image.load('D.png').convert())
    D = pygame.transform.scale(D, (100,100))
    D.set_colorkey((0,0,0))
#câu hỏi nhiệm vụ
    answer_duty_true=[pygame.image.load('answer_true.jpg').convert_alpha(),True]#đáp án đúng
    answer_duty_true[0]=pygame.transform.scale(answer_duty_true[0],(400,200))
    answer_duty_true[0].set_colorkey((0,0,0))
    answer_duty_false1=[pygame.image.load('answer_false1.jpg').convert_alpha(),False]#đ.án sai
    answer_duty_false1[0]=pygame.transform.scale(answer_duty_false1[0],(400,200))
    answer_duty_false1[0].set_colorkey((0,0,0))
    answer_duty_false2=[pygame.image.load('answer_false2.jpg').convert_alpha(),False]#đ.án sai
    answer_duty_false2[0]=pygame.transform.scale(answer_duty_false2[0],(400,200))
    answer_duty_false2[0].set_colorkey((0,0,0))
    answer_duty_false3=[pygame.image.load('answer_false3.jpg').convert_alpha(),False]#đ.án sai
    answer_duty_false3[0]=pygame.transform.scale(answer_duty_false3[0],(400,200))
    answer_duty_false3[0].set_colorkey((0,0,0))
    answer_duty_list=[answer_duty_true,answer_duty_false1,answer_duty_false2,answer_duty_false3]#ds đ.án
    answer=-1
    choose=None
#kết quả nv
    wrong=(pygame.image.load('wrong1.png').convert())
    wrong = pygame.transform.scale(wrong, (SCREEN_WIDTH,SCREEN_HEIGHT))
    wrong.set_colorkey((0,0,0))
    ques=0#đếm câu hỏi
#bộ câu hỏi
    question1=(pygame.image.load('question1.jpg').convert_alpha())
    question1=pygame.transform.scale(question1,(550,SCREEN_HEIGHT))
    question1.set_colorkey((0,0,0))
#hiển thị mode 2
    mode2=0
#câu hỏi 1
    answer1_true=[pygame.image.load('answer_true.png').convert_alpha(),True]
    answer1_true[0]=pygame.transform.scale(answer1_true[0],(400,200))
    answer1_true[0].set_colorkey((0,0,0))
    answer1_false1=[pygame.image.load('answer_false1.png').convert_alpha(),False]
    answer1_false1[0]=pygame.transform.scale(answer1_false1[0],(400,200))
    answer1_false1[0].set_colorkey((0,0,0))
    answer1_false2=[pygame.image.load('answer_false2.png').convert_alpha(),False]
    answer1_false2[0]=pygame.transform.scale(answer1_false2[0],(400,200))
    answer1_false2[0].set_colorkey((0,0,0))
    answer1_false3=[pygame.image.load('answer_false3.png').convert_alpha(),False]
    answer1_false3[0]=pygame.transform.scale(answer1_false3[0],(400,200))
    answer1_false3[0].set_colorkey((0,0,0))
    answer1_list=[answer1_true,answer1_false1,answer1_false2,answer1_false3]
    answer1=-1
    choose=None
#câu hỏi 2
    answer2_true=[pygame.image.load('answer2_true.png').convert_alpha(),True]
    answer2_true[0]=pygame.transform.scale(answer2_true[0],(400,200))
    answer2_true[0].set_colorkey((0,0,0))
    answer2_false1=[pygame.image.load('answer2_false1.png').convert_alpha(),False]
    answer2_false1[0]=pygame.transform.scale(answer2_false1[0],(400,200))
    answer2_false1[0].set_colorkey((0,0,0))
    answer2_false2=[pygame.image.load('answer2_false2.png').convert_alpha(),False]
    answer2_false2[0]=pygame.transform.scale(answer2_false2[0],(400,200))
    answer2_false2[0].set_colorkey((0,0,0))
    answer2_false3=[pygame.image.load('answer2_false3.png').convert_alpha(),False]
    answer2_false3[0]=pygame.transform.scale(answer2_false3[0],(400,200))
    answer2_false3[0].set_colorkey((0,0,0))
    answer2_list=[answer2_true,answer2_false1,answer2_false2,answer2_false3]
    answer2=-1
#câu hỏi 3
    answer3_true=[pygame.image.load('answer2_false1.png').convert_alpha(),True]
    answer3_true[0]=pygame.transform.scale(answer3_true[0],(400,200))
    answer3_true[0].set_colorkey((0,0,0))
    answer3_false1=[pygame.image.load('answer2_true.png').convert_alpha(),False]
    answer3_false1[0]=pygame.transform.scale(answer3_false1[0],(400,200))
    answer3_false1[0].set_colorkey((0,0,0))
    answer3_false2=[pygame.image.load('answer2_false2.png').convert_alpha(),False]
    answer3_false2[0]=pygame.transform.scale(answer3_false2[0],(400,200))
    answer3_false2[0].set_colorkey((0,0,0))
    answer3_false3=[pygame.image.load('answer2_false3.png').convert_alpha(),False]
    answer3_false3[0]=pygame.transform.scale(answer3_false3[0],(400,200))
    answer3_false3[0].set_colorkey((0,0,0))
    answer3_list=[answer3_true,answer3_false1,answer3_false2,answer3_false3]
    answer3=-1

    wrong_mode2=(pygame.image.load('wrong_mode2.png').convert_alpha())
    wrong_mode2=pygame.transform.scale(wrong_mode2,(SCREEN_WIDTH,SCREEN_HEIGHT))
    wrong_mode2.set_colorkey((0,0,0))
    wrong_mode1=(pygame.image.load('wrong1.png').convert_alpha())
    wrong_mode1.set_colorkey((0,0,0))

    def sort_answer(answer_list):
        another_list=answer_list
        oder_answer_list=[]
        for i in range(len(another_list)):
            oder_number=random.choice(answer_list)
            oder_answer_list.append(oder_number)
            another_list.remove(oder_number)
        
        return oder_answer_list


    def player_move_right(player,player_x,key,player_x_no_move,oject_x,stopper_x):
        if key[pygame.K_j]:#dư
            if player_x<=1295:
                player_x+=5
                if player_x%10==0:
                    player=pygame.image.load('player_walk_right1.png').convert_alpha()
                    player=pygame.transform.scale(player,(100,175))
                else:
                    player=pygame.image.load('player_walk_right2.png').convert_alpha()
                    player=pygame.transform.scale(player,(100,175))
            else:
                if not (player_x==stopper_x+200):
                    player_x_no_move+=5
                    if player_x_no_move%2==0:
                        player=pygame.image.load('player_walk_right1.png').convert_alpha()
                        player=pygame.transform.scale(player,(100,175))
                        oject_x-=5
                    else:
                        player=pygame.image.load('player_walk_right2.png').convert_alpha()
                        player=pygame.transform.scale(player,(100,175))
                        oject_x-=5
            

        return player,player_x,player_x_no_move,oject_x,stopper_x



    def player_move_left(player,player_x,key,player_x_no_move,oject_x,home_x):
        if player_x>=0:
            player_x-=5
            if player_x%10==0:
                player=pygame.image.load('player_walk_left1.png').convert_alpha()
                player=pygame.transform.scale(player,(100,175))
            else:
                player=pygame.image.load('player_walk_left2.png').convert_alpha()
                player=pygame.transform.scale(player,(100,175))
        else:
            if not (player_x<=home_x):
                player_x_no_move-=5
                if player_x_no_move%20==0:
                    player=pygame.image.load('player_walk_left1.png').convert_alpha()
                    player=pygame.transform.scale(player,(100,175))
                    oject_x+=5
                else:
                    player=pygame.image.load('player_walk_left2.png').convert_alpha()
                    player=pygame.transform.scale(player,(100,175))
                    oject_x+=5
        
        return player,player_x,player_x_no_move,oject_x,home_x


    def answer_apear(oder_answer_list):
        screen.blit(oder_answer_list[0][0],(600,75))
        screen.blit(oder_answer_list[1][0],(1000,75))
        screen.blit(oder_answer_list[2][0],(600,325))
        screen.blit(oder_answer_list[3][0],(1000,325))
        #hiện ABCD
        screen.blit(A,(600,75))
        screen.blit(B,(1000,75))
        screen.blit(C,(600,325))
        screen.blit(D,(1000,325))


    def answer_duty_apear(oder_answer_list):
        screen.blit(oder_answer_list[0][0],(300,75))
        screen.blit(oder_answer_list[1][0],(900,75))
        screen.blit(oder_answer_list[2][0],(300,325))
        screen.blit(oder_answer_list[3][0],(900,325))
        #hiện câu hỏi ABCD
        screen.blit(A,(300,75))
        screen.blit(B,(900,75))
        screen.blit(C,(300,325))
        screen.blit(D,(900,325))


    def choose_answer_duty1(oder_answer_list,choose,answer):
        if oder_answer_list[0][0].get_rect(topleft=(300, 75)).collidepoint(event.pos):
            choose=oder_answer_list[0]
            if oder_answer_list[0][1]:
                answer=0
            else:
                answer=1
        if oder_answer_list[1][0].get_rect(topleft=(900, 75)).collidepoint(event.pos):
            choose=oder_answer_list[0]
            if oder_answer_list[1][1]:
                answer=0
            else:
                answer=1
        if oder_answer_list[2][0].get_rect(topleft=(300, 325)).collidepoint(event.pos):
            choose=oder_answer_list[0]
            if oder_answer_list[2][1]:
                answer=0
            else:
                answer=1
        if oder_answer_list[3][0].get_rect(topleft=(900, 325)).collidepoint(event.pos):
            choose=oder_answer_list[0]
            if oder_answer_list[3][1]:
                answer=0
            else:
                answer=1
        return answer

    def choose_answer1(oder_answer_list,choose,answer):
        if oder_answer_list[0][0].get_rect(topleft=(600,75)).collidepoint(event.pos):
            choose=oder_answer_list[0]
            if oder_answer_list[0][1]:
                answer=0
            else:
                answer=1
        if oder_answer_list[1][0].get_rect(topleft=(1000,75)).collidepoint(event.pos):
            choose=oder_answer_list[0]
            if oder_answer_list[1][1]:
                answer=0
            else:
                answer=1
        if oder_answer_list[2][0].get_rect(topleft=(600,325)).collidepoint(event.pos):
            choose=oder_answer_list[0]
            if oder_answer_list[2][1]:
                answer=0
            else:
                answer=1
        if oder_answer_list[3][0].get_rect(topleft=(1000,325)).collidepoint(event.pos):
            choose=oder_answer_list[0]
            if oder_answer_list[3][1]:
                answer=0
            else:
                answer=1
        return answer


    def choose_answer_duty2(answer,wrong,duty):
        if answer==0:
            duty+=2
        elif answer==1:
            screen.blit(wrong,(0,0))
        return duty
    def choose_answer2(answer,wrong,ques):
        if answer==1:
            screen.blit(wrong,(0,0))
        elif answer==0:
            ques+=1
        return ques


#main programe
    run=True
    oder_answer_duty_list=sort_answer(answer_duty_list)
    oder_answer_list1=sort_answer(answer1_list)
    oder_answer_list2=sort_answer(answer2_list)
    oder_answer_list3=sort_answer(answer3_list)
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
        screen.blit(note4,(2400 + oject_x,550))

        if key[pygame.K_j]:
            player,player_x,
            player,player_x,player_x_no_move,oject_x,stopper_x=player_move_right(player,player_x,key,player_x_no_move,oject_x,stopper_x)
        
    
        elif key[pygame.K_f]:
            player,player_x,player_x_no_move,oject_x,home_x=player_move_left(player,player_x,key,player_x_no_move,oject_x,home_x)
        screen.blit(player,(player_x,535))
        screen.blit(home2,(oject_x,0))
        screen.blit(way3,(oject_x,20))
        screen.blit(way4,(oject_x+1500,20))

        if player_x==home_x:
            run=True
            runing=-1
            ques=0
            while run:
            
                screen.fill((250,250,250))
                if ques==0:
                    ques=0
                    answer_apear(oder_answer_list1)
                    ques=choose_answer2(answer1,wrong_mode2,ques)
                
        
                elif ques==1:
                    question1=(pygame.image.load('question2.jpg').convert_alpha())
                    question1=pygame.transform.scale(question1,(550,SCREEN_HEIGHT))
                    question1.set_colorkey((0,0,0))
                    answer_apear(oder_answer_list2)
                    ques=choose_answer2(answer2,wrong_mode2,ques)
        
                elif ques==2:
                    question1=(pygame.image.load('question3.jpg').convert_alpha())
                    question1=pygame.transform.scale(question1,(550,SCREEN_HEIGHT))
                    question1.set_colorkey((0,0,0))
                    answer_apear(oder_answer_list3)
                    ques=choose_answer2(answer3,wrong_mode2,ques)
                elif ques==3:
                    run= False
                    player_x=700
                screen.blit(question1,(0,0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run= False
                        runing=0
                
    

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if ques == 0:
                            answer1 = choose_answer1(oder_answer_list1, choose, answer1 )
                        elif ques == 1:
                            answer2 = choose_answer1(oder_answer_list2, choose, answer2)
                        elif ques == 2:
                            answer3 = choose_answer1(oder_answer_list3, choose, answer3)
                pygame.display.flip()

            if runing==0:
                pygame.quit()
            else:
                run=True   

        if key[pygame.K_r]:
            player_x=700
            oject_x=0
            

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
            answer_duty_apear(oder_answer_duty_list)
            screen.blit(note3,(460,100))
            duty=choose_answer_duty2(answer, wrong_mode1,duty)

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
    
        if duty >= 0:
            if duty<=4:
                screen.blit(duty_box, (0, 200))




    
     
    
    #DIEU CHINH
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and duty == 2:
                answer = choose_answer_duty1(oder_answer_duty_list, choose, answer)
        pygame.display.flip()
        await asyncio.sleep(0)
        clock.tick(60)
    pygame.quit()
if __name__=='__main__':
    asyncio.run(main())
