# fancy.py
# Asks the user for their first, last, and nickname, then welcomes the user
#
# Tyler Robertson
# January 4, 2013

def main() :
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    nick = input("Enter your nickname: ")
    print("Welcome back, ",first," \"",nick,"\" ",last,"!",sep='')

main()
