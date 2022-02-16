import random
random_number=random.randint(1,9)
Magic_8_Balls_answer=[
'Yes-definitely.','It is decidedly so.',
'Without a doubt.','Reply hazy, try again.',
'Ask again later.','Better not tell you now.',
'My sources say no.',
'Outlook not so good.',
'Very doubtful.'
]
Name= input('What is your name? ')
Question = input('What is the Question? ')
if Name and Question ==True:
    print(random_number)
if random_number == 1:
        Magic_8_Balls_answer=Magic_8_Balls_answer[0]
elif random_number == 2:
        Magic_8_Balls_answer=Magic_8_Balls_answer[1]
elif random_number == 3:
        Magic_8_Balls_answer=Magic_8_Balls_answer[2]
elif random_number == 4:
        Magic_8_Balls_answer=Magic_8_Balls_answer[3]
elif random_number == 5:
        Magic_8_Balls_answer=Magic_8_Balls_answer[4]
elif random_number == 6:
        Magic_8_Balls_answer=Magic_8_Balls_answer[5]
elif random_number == 7:
        Magic_8_Balls_answer=Magic_8_Balls_answer[6]
elif random_number == 8:
        Magic_8_Balls_answer=Magic_8_Balls_answer[7]
elif random_number == 9:
        Magic_8_Balls_answer=Magic_8_Balls_answer[8]
else:
    print('ERROR')
print(Name,':',Question,':',Magic_8_Balls_answer)