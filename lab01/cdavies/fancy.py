# helloworld.py
# Say a fancy hello to the user.
#
# Connor Davies
# 1/5/13

def main() :
    fname = input("Enter your first name: ") #Get first name from user.
    lname = input("Enter your last name: ") #Get last name from user.
    nname = input("Enter your nickname: ") #Get nickname from user.
    print("Welcome back, " + fname + " \"" + nname + "\" " + lname + "!")
    
main()