import pygame
import random
pygame.init()
width=1500
height=600
screen=pygame.display.set_mode((width,height))
ques=0#đếm câu hỏi
#bộ câu hỏi
question1=(pygame.image.load('question1.jpg').convert_alpha())
question1=pygame.transform.scale(question1,(550,height))
question1.set_colorkey((0,0,0))
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
answer=-1
choose=None
#câu hỏi 2
answer2_true=[pygame.image.load('answer2_true.png').convert_alpha(),True]
answer2_true[0]=pygame.transform.scale(answer1_true[0],(400,200))
answer2_true[0].set_colorkey((0,0,0))
answer2_false1=[pygame.image.load('answer2_false1.png').convert_alpha(),False]
answer2_false1[0]=pygame.transform.scale(answer1_false1[0],(400,200))
answer2_false1[0].set_colorkey((0,0,0))
answer2_false2=[pygame.image.load('answer2_false2.png').convert_alpha(),False]
answer2_false2[0]=pygame.transform.scale(answer1_false2[0],(400,200))
answer2_false2[0].set_colorkey((0,0,0))
answer2_false3=[pygame.image.load('answer2_false3.png').convert_alpha(),False]
answer2_false3[0]=pygame.transform.scale(answer1_false3[0],(400,200))
answer2_false3[0].set_colorkey((0,0,0))
answer2_list=[answer2_true,answer2_false1,answer2_false2,answer2_false3]
answer2=-1
#đáp án 1
congratulation=(pygame.image.load('congratulation1.jpg').convert())
wrong=(pygame.image.load('wrong1.png').convert())

def sort_answer(answer_list):
    choices = list(answer_list)
    ordered_list = []
    while choices:
        next_choice = random.choice(choices)
        ordered_list.append(next_choice)
        choices.remove(next_choice)
    return ordered_list


def answer_apear(oder_answer_list):
    screen.blit(oder_answer_list[0][0],(600,75))
    screen.blit(oder_answer_list[1][0],(1000,75))
    screen.blit(oder_answer_list[2][0],(600,325))
    screen.blit(oder_answer_list[3][0],(1000,325))


def choose_answer1(oder_answer_list,choose,answer,mouse_pos):
    positions=[(600,75),(1000,75),(600,325),(1000,325)]
    for index, option in enumerate(oder_answer_list):
        rect=option[0].get_rect(topleft=positions[index])
        if rect.collidepoint(mouse_pos):
            choose=option
            return 0 if option[1] else 1
    return answer

def choose_answer2(answer,congratulation,wrong,ques):
    if answer==1:
        screen.blit(wrong,(300,75))
    elif answer==0:
        ques+=1
    return ques


oder_answer_list1=sort_answer(answer1_list)
oder_answer_list2=[]
for i in range(len(answer2_list)):
        oder_number=random.choice(answer2_list)
        oder_answer_list2.append(oder_number)
        answer2_list.remove(oder_number)
print(oder_answer_list2[0][1])
run=True
while run:
    screen.fill((250,250,250))
    if ques==0:
        answer_apear(oder_answer_list1)
        ques=choose_answer2(answer,congratulation,wrong,ques)
        answer=-1
        
    elif ques==1:
        question1=(pygame.image.load('question2.jpg').convert_alpha())
        question1=pygame.transform.scale(question1,(550,height))
        question1.set_colorkey((0,0,0))
        answer_apear(oder_answer_list2)
        ques=choose_answer2(answer2,congratulation,wrong,ques)
    screen.blit(question1,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ques == 0:
                answer = choose_answer1(oder_answer_list1, choose, answer, event.pos)
            elif ques == 1:
                answer2 = choose_answer1(oder_answer_list2, choose, answer2, event.pos)
     
        
        
    pygame.display.flip()

pygame.quit()
