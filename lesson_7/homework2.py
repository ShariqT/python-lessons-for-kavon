# This program is almost done. You need to add an if/else statement
# somewhere in the program so that if I enter a number
# that is greater than or equal to 5, then the magic number
# is 80. If the number is anything else then the magic 
# number is 18
# You are only allowed to add the if/else statement. You are not allowed
# to change any of the variables or the if/else statment that is already
# in the program.
number_list = input("What is the starting magic number: ")
int_list_1 = [8, 9, 2, 5, 10]
int_list_2 = [3, 8, 10, 1, 6]
if number_list < str(5):
    series_of_numbers = int_list_2
else:
    series_of_numbers = int_list_1
if series_of_numbers[4] / series_of_numbers[2] > 5:
    print("magic numbe r is")
    print(series_of_numbers[1] * series_of_numbers[3])
else:
    print("magic number is")
    print(series_of_numbers[0] * series_of_numbers[4])