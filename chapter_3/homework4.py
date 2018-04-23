# Kavon, I want seprate the float_list variable into two parts -- one 
# that prints out all numbers that are less that 10 and ones that are 
# more than 10. 
# If the user enters the word "above", then print out all of numbers in
# float_list that are more than 10. If the user enters the word "below", then
# print out all of the numbers in float_list that re less than 10. 
# Hint: you can only add to this progam, you cannot edit/change the
# float_list variable or the my_selection variable

my_selection = input("How do you want to filter? ")
float_list = [ 2.1, 3.2, 44.0, 12.1, 3.8, 8.33 ]
float_list1 = [ 2.1, 3.2, 3.8, 8.33 ] 
float_list2 = [44.0, 12.1 ]

if my_selection == str("above"):
    #print(float_list2)
    counter  = 0
    while counter < len(float_list):
        if float_list[counter] > 10.0:
            print(float_list[counter])
        counter +=1
    

if my_selection == str("below"):
    #print(float_list1)
    counter  = 0
    while counter < len(float_list):
        if float_list[counter] < 10.0:
            print(float_list[counter])
        counter +=1
