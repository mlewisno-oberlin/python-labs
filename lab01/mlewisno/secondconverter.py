# secondconverter.py
# Converts seconds into more readable hours, minutes and seconds
#
# Mischa Lewis-Norelle
# January 6th 2013

def main():
    sec = eval(input("Please enter a number of seconds: "))
    hour = sec // 3600
    sec = sec % 3600
    min = sec // 60
    sec = sec % 60
    print(hour, "Hours", min, "Minutes and", sec, "Seconds")
    
main()