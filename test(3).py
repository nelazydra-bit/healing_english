import random
answer_list=[1,2,3,4]
oder_answer_list=[]
for i in range(4):
        oder_number=random.choice(answer_list)
        oder_answer_list.append(oder_number)
        answer_list.remove(oder_number)
print(answer_list,oder_answer_list)
