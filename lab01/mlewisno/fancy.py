# fancy.py
# Says hello to the world with enthusiasm using the user's name (after prompt)
#
# Mischa Lewis-Norelle
# January 6th 2013

def main():
    firstName = input("Please enter your first name User: ")
    nickName = input("Please enter your nickname User: ")
    lastName = input("Please enter your last name User: ")
    print("Welcome back,", firstName, "\"", nickName, "\"", lastName, "!")
    
main()