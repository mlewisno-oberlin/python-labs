# secondconverter.py
# Translate seconds into a more readable hours, minutes, and seconds
#
# Tyler Robertson
# January 4, 2013

def main() :
    print("This program translates seconds")
    print("into a more readable hours, minutes, and seconds.")
    sec = eval(input("Input total number of seconds: "))
    s = sec % 60
    h = sec//3600
    nsec = sec - (h * 3600)
    m = nsec//60
    print(sec,"seconds is equal to",h,"hours,",m,"minutes, and",s,"seconds.")
    
main()
