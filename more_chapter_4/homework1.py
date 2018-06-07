# using a for loop, make a program that will add the 
# letters 'at' to each string in my_list and print out
# the result. So, the first thing that should be printed out
# is 'cat' and the second is 'hat' and so on.
# Note: you cannot change the variable my_list. You can do
# everything else though

my_list = ['c', 'h', 'd', 'p', 'b', 'e' ]
food = ['cookeies', 'piazza', 'coke', 'candy', 'fruit']
add_on = "at"
letter = my_list

for letter in range(0, len(my_list)):
    print (my_list[letter] + food[letter])  