# _*_ coding: utf-8 _*_

import os

def say_hello():
    print "Hi"

def print_3():
    print "1 2 3"

def foo():
    for i in range(0, 100):
        print "Hello %d" % i 

def my_exit():
    # Close opened files
    # Close databases connections
    # Confirm by user
    # Save session variables
    # Emit messages for exit
    if raw_input("Do you want to exit? ") == "no":
        menu()
    else:
        print "Bye!"

def menu():
    os.system("clear")
    print "A. Say Hello"
    print "B. Print 3 numbers"
    print "C. Call Foo"
    print "X. Exit"
    print

    opt = raw_input("> ")

    if opt == "A":
        say_hello()
    elif opt == "B":
        print_3()
    elif opt == "C":
        foo()
    elif opt == "X":
        my_exit() # exit() is defined by python, don't use it
        return # This "return" breaks the function and ends it
    else:
        print "The option is invalid"
        raw_input("press any key to continue...")
        
    raw_input("press any key to continue...")
    menu() # Most logic way is to repeat the menu() until breaks manually

# Call function to start the program
menu()