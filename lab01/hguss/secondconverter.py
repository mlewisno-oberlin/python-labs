# secondconverter.py
# converts an amount of seconds into a more readable format
#
# Henry Lionni Guss
# 1/3/12

def main():
    sec = eval(input("Enter a number of seconds: "))
    seconds = sec % 60
    minutes = (sec // 60) % 60
    hours = sec // 3600
    print(sec, "seconds is equal to", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
    
main()