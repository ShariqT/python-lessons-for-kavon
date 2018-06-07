# This is good size project and may take a you a couple of days to finish,
# but ties in a bunch that we have learned so far.
# I want you to make a program will help me learn my times tables
# the program should:
# 1) Ask me which times tables am I trying to learn. 
# 2) Then it will ask me three random math questions about
# that times table. So for example, if I enter in that I am trying to
# learn the 2's time tables, the program will ask me three math questions
# about the 2's time tables like 2 x 3 or 2 x 8 or 2 x 2. The math questions
# must be random.  I don't want you ask me the same math questions over and 
# over. 
# 3) after answering the questions, it will give me a score, like 
# "got 2 out 3 answers correct" and then print out the percentage correct.


import random

table = input("What times table would you like to learn? ")
random_1 = random.randint(1,10)
random_2 = random.randint(1,10)
random_3 = random.randint(1,10)
random_number = [random_1, random_2, random_3]
answers = []
correct_answer = []
final_correct_answers = 0
for i in random_number:
    user_answer = input("What is " + str(i) + "*" + table +" " )
    answers.append(int(user_answer))
    correct_answer.append(i * int(table))
if answers == correct_answer:
    print("You did that bitch!")
    
if answers[0] == correct_answer[0]:
    final_correct_answers+=1
if answers[1] == correct_answer[1]:
    final_correct_answers+=1
if answers[2] == correct_answer[2]:
    final_correct_answers+=1

if final_correct_answers == 1:
    print("YOu fucked up twice!")    
elif final_correct_answers == 2:
    print("You fucked up once!")
else:
    print("You fucking suck!")
