In this lesson you will learn:

how to make a program that makes decisons


Instructions:

In python, you can make your programs branch in different way depending on a variable by using the "if" statement. Here is an example of it being used...

        a = 0
        if a > 0:
            print("a is more than zero")

Now there are a few things to note here. One, you have to tab the next line after you do a "if" statement. The tabbed portion is what is called a "block". This basically tells the computer that if the line above, a > 0 is true, then do everything that is within that block. 

You can even add an "else" statement and the program will branch in two ways...

        a = 0
        if a > 0:
            print("a is more than zero")
        else:
            print("a is not more than zero")

You can add another 'if' statement by using 'elif' after the first 'if' statement. The following is an example....

        a = 7
        if a < 5:
            print("a is less than 5")
        elif a == 6:
            print("a is 6")
        elif a == 7:
            print("a is 7")
        else: 
            print("a is more than 7")

The above program will print out "a is 7" because none of the other "if" and "elif" statements were true. 

If you change the variable "a" to 10, then the program will print out "a is more than 7". Think of the "else" the last stop on a decision branch. Since of none of the other conditions were met, then the program opted to do what is in the "else" block. 

Also notice that if you want to check to see if something is equal to another thing, you have to use the double equal signs ( == ) to do so. That is because as we learned in the previous lesson, you assign a variable a value by using one equal sign ( = ). If you find yourself mixing up the two, don't worry about it. Its's a common mistake that happens when you are first learning. 

Homework:

I want to you write a program that will let me enter in my name. Use the "if" and "else" statements to check to see if the person entered "shariq". If they did, then I want the program to print "Access Granted" and "Welcome, Mr. Torres". If anything other than "shariq", then I want the program to say, "Access Denied". 



