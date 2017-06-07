import os

def menu():
    os.system("clear")
    print "Select an option"
    print "1. Add contact"
    print "2. Find contact"
    print "3. Update contact"
    print "4. Delete contact"
    print "-" * 40
    print "x. Exit"
    print

    opt = raw_input("> ")

    if opt == "1":
        add_contact() # Delegate functionality to add_contact()
    elif opt == "2":
        find_contact()
    elif opt == "3":
        update_contact()
    elif opt == "4":
        delete_contact()
    elif opt == "x":
        print "Bye!"
        return
    else:
        print "Invalid option"
    
    raw_input("press any key to continue...")
    menu()

menu()