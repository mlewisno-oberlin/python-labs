# secondconverter.py
# Translate seconds into a more readable hours, minutes, and seconds.
# 
# Samantha Mater
# 3 January 2013
   
def main() :
    MIN_LEN = 60 #seconds in a minute
    HR_LEN = 60 #minutes in an hour
    print("Takes an input of seconds and returns the hours, minutes, and seconds.")
    sec = eval(input("Enter a positive amount of seconds: "))
    s = sec % MIN_LEN
    m = (sec//MIN_LEN) % HR_LEN
    h = sec//(HR_LEN*MIN_LEN)
    print(h, "hours,", m, "minutes,", s, "seconds.")
main()

# to change this in the future, I might make a minutes variable and an hour variable
# and use those as static final variables (as done above)