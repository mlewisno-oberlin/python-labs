# fancy.py
# Greets a person in a better manner
#
# Henry Lionni Guss
# 1/3/12

def main():
    firstName = input("What is your first name?")
    lastName = input("What is your last name?")
    nickname = input("What is your nickname?")
    print("Welcome back, ", firstName, " \"", nickname, "\" ", lastName, "!", sep='', end='')
    
main()