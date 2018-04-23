
#CHAPTER2
#complete favorite_food = input("what is your favorite food?")
#complete print(favorite_food)
#complete favorite_food2 = input("what is your second favorite food? ")
#complete print(favorite_food2) 
#complete print(favorite_food + favorite_food2)

#complete total_bill = input("what's the total bill? ")
#complete x = float(total_bill)
#complete tip_fifteen = x*.15
#complete tip_fifteen = int(tip_fifteen)
#complete tip_twenty = x*.20
#complete tip_twenty = int(tip_twenty)
#complete print("A 15% tip is", int(tip_fifteen), "dollars.")
#complete print("A 20% tip is", int(tip_twenty), "dollars.")
#completeprint("Your total bill plus a 15% tip is", float(total_bill)+int(tip_fifteen), "dollars.")
#complete print("Your total bill plus a 20% tip is", float(total_bill)+int(tip_twenty), "dollars")

#CHAPTER 3
#import random

#fortune_1 = "You will be wealthy for the rest of your life"
#fortune_2 = "You will meet the love of your life"
#fortune_3 = "You will live in a huge mansion right by the water"
#fortune_4 = "You will land your dream career"
#fortune_5 = "You will have two healthy children, a boy and a girl"
#fortunes = random.randint(0,4)
#my_list = [fortune_1, fortune_2, fortune_3, fortune_4, fortune_5]
#print(my_list[fortunes])

# import random
# counter = 0
# heads = 1
# tales = 2
# number_heads = 0
# number_tales = 0
# while counter <= 99:
#     heads_or_tales = random.randint(1,2)
#     if heads_or_tales == heads:
#         number_heads+=1
#     if heads_or_tales == tales:
#         number_tales+=1
#     counter+=1
# print(number_heads)
# print(number_tales)
# import random
# print("Im guessing of a number between 1 and 100, what is my number")
# number = random.randint(1, 100)
# max_tries = 2
# attempts = 1

# while attempts <= max_tries:
#     guess = input("What is my number?")
#     if guess != number:
#         print("HELL NO!!! YOU FAILED HORRIBLY ASSHOLE!")
#     if guess == number:
#         print("Congrats asshole, you did it!")
#         break
#     attempts+=1
# print("You have no more attempts, Game Over Asshole!")
# print("the correct number is" + str(number))


#Chaper4

import random
start_number = input("What is your starting number? ")
end_number = input("what is your ending number? ")
count_number = input("how much should I count by? ")

for k in range(int(start_number),int(end_number),int(count_number)):
    print(k)
    
 