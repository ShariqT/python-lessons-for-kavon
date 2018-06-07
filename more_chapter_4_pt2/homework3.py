# make a program that will let me enter a number and then
# print out all of the multiples until 100. So, if I enter a 2, 
# then the program should print out all of the multiples of 2 until 100. 
# If I enter a 8, then the program should print out all of the multiples of
# 8 until 100. 


number = input("what is your number? ")

for i in range(0,101,int(number)):
    print(i)

    