So far, we have been working with one type of data -- a string. The string has the quotation marks around it and is usally used to print stuff to the screen and display messages. 

But now, we are going to work with another type of data -- a list. A list is a collection of other types of data. So, you can have a list of strings (letters, words) or a list of numbers. Here is an example of how to use a list....


    myList = ["k","a","v","o","n"]
    print(myList)


Lists are what is called "zero-indexed". That means that instead of starting at 1, you start at 0 when using lists. So, if I wanted to print out the "v" in the "myList" variable, I would have to find the index first. Look at the example below (Note* this is not code. This is a illustration to show you how the counting in lists works. Don't copy this part into the editor)...

    ["k", "a", "v", "o", "n"]
    [ 0    1    2    3    4 ]


As you can see, the "v" is at index 2. To print out that letter, I would need to do the following...

    myList = ["k","a","v","o","n"]
    print(myList[2])


You can access all of the different letters like this. Now, your name only has five letters. What happens if we try to access something that is bigger than the list? Try out this program and see what happens....

    myList = ["k","a","v","o","n"]
    print(myList[100])

This program will fail with an IndexError. This means you tried to get something outside of the bounds of the list. To get the length of a list you can do use the "len" function. This function takes a list as the only parameter. Here is an example...

    myList = ["k","a","v","o","n"]
    myListLength = len(myList)
    print(myListLength)
This will output the number 5. Now one thing to remember is that when you get the length of a list, Python reverts back to regular counting, i.e., beginning on 1 instead of 0.  

Now one thing you need to know is that in Python, the strings that we have been using before can ALSO be used as a list. 
You can do find print out the "v" in "kavon" by using a list...

    myList = ["k","a","v","o","n"]
    print(myList[2])

Or by using a string...

    myString = "kavon"
    print(myString[2])

Both programs will output the same thing!

Homework:
So we are going to extend the program that we wrote to get the user's full name and username in Lesson 1. Copy that file into this folder and rename it. 

So, now what I want is to generate a password for people based off of their full name and username. I want to you make it so that you generate a user's password off of the 1st, 4th, and 5th index of the their full name and the 1st and last letter of their username. So, if you ran the program and entered: "Kavon Ward" for the full name and "kward1025" as the username, your password would be "Konk5". When you have the password, print it out with the rest of the information that the user entered. 

=====================
HINT: You can join two strings together by using the "+" sign. For example, this program...
    
    print("hello" + " world")
    print("hello" + "world")

Will display "hello world" and right underneath display "helloworld".
================

