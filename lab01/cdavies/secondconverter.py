# secondconverter.py
# Translate seconds into a more readable hours, minutes, and seconds.
# 
# Connor Davies
# 1/6/13

def main() :
    print("")
    print("Welcome to my Second Converter!")
    print("")
    print("This program will properly calculate the number of minutes and seconds under 60 from a given number of seconds.") # Explain on the terminal (via print function) what this program does.
    print("")
    n = eval(input("Please enter a nonnegative number of seconds:")) # Prompt the user to enter a number of seconds, store in a variable.
    h = n//3600 # Compute hours
    m = (n-(h*3600))//60 # Compute minutes
    s = (n-(h*3600)-(m*60)) # compute seconds
    print(h, " hours ", m, " minutes", s, "seconds") # Print the results.
    
main()