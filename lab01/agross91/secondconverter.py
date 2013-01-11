# Allison Gross
# secondconverter.py
# Converts seconds into hours, minutes and seconds
# 01-07-13

def main():
    print("Welcome to the Second Converter!")
    print()
    print("This program will properly calculate the number of hours \nminutes and seconds from a given number of seconds")
    print()
    
    s = eval(input("Enter the number of seconds to convert: "))
    seconds = s%60
    minutes = (s//60)%60
    hours = s//3600
    
    print(s, "seconds is equal to", hours, "hours", minutes, "minutes and", seconds, "seconds")

main()
    