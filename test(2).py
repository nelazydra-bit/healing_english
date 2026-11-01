import pygame
import random
pygame.init()
width=1500
height=600
run=True
screen=pygame.display.set_mode((width,height))
answer_true=[pygame.image.load('answer_true.jpg').convert(),True]
answer_true[0]=pygame.transform.scale(answer_true[0],(400,200))
answer_false1=[pygame.image.load('answer_false1.jpg').convert(),False]
answer_false1[0]=pygame.transform.scale(answer_false1[0],(400,200))
answer_false2=[pygame.image.load('answer_false2.jpg').convert(),False]
answer_false2[0]=pygame.transform.scale(answer_false2[0],(400,200))
answer_false3=[pygame.image.load('answer_false3.jpg').convert(),False]
answer_false3[0]=pygame.transform.scale(answer_false3[0],(400,200))
answer_list=[answer_true,answer_false1,answer_false2,answer_false3]
answer=-1

congratulation=(pygame.image.load('congratulation1.jpg').convert())
duty=-1

wrong=(pygame.image.load('wrong1.jpg').convert())

choose=None

def answer_apear(oder_answer_list):
    screen.blit(oder_answer_list[0][0],(300,75))
    screen.blit(oder_answer_list[1][0],(900,75))
    screen.blit(oder_answer_list[2][0],(300,325))
    screen.blit(oder_answer_list[3][0],(900,325))
def sort_answer(answer_true,answer_false1,answer_false2,answer_false3):
    answer_list=[answer_true,answer_false1,answer_false2,answer_false3]
    ordered_list=[]
    choices=list(answer_list)
    while choices:
        next_choice=random.choice(choices)
        ordered_list.append(next_choice)
        choices.remove(next_choice)
    return ordered_list



def choose_answer1(oder_answer_list,choose,answer,mouse_pos):
    positions=[(300, 75),(900, 75),(300, 325),(900, 325)]
    for index, option in enumerate(oder_answer_list):
        rect=option[0].get_rect(topleft=positions[index])
        if rect.collidepoint(mouse_pos):
            choose=option
            return 0 if option[1] else 1
    return answer


def choose_answer2(answer,congratulation,wrong):
    if answer==0:
        screen.blit(congratulation,(300,75))
    elif answer==1:
        screen.blit(wrong,(300,75))

#để ngoài while
oder_answer_list=sort_answer(answer_true,answer_false1,answer_false2,answer_false3)

while run:
    
    answer_apear(oder_answer_list)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
#phần nghi bị lỗi
        if event.type==pygame.MOUSEBUTTONDOWN:
            answer=choose_answer1(oder_answer_list,choose,answer,event.pos)
    choose_answer2(answer,congratulation,wrong)
    pygame.display.flip()
#mong cô hỗ trợ ạ
                
pygame.quit()



