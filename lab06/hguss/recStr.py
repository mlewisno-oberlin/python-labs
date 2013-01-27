# recNum.py
# Performs recursive number operations
#
# Henry Lionni Guss
# 1/25/13

def main():
    print("This program will print a string backwards, determine whether or not it",
        "is a palindrome, and determine whether or not a second string is within it.")
    s, t = input("Enter two strings(seperated by commas): ")
    print("The string \"", s, "\" backwards is ", backwards(s), ".", sep = '')
    if palindrome(s) == True:
        print("The string \"", s, "\" is a palindrome.", sep = '')
    else:
        print("The string \"", s, "\" is not a palindrome.", sep = '')
    if substring(s, t) == True:
        print("The string \"", t, "\" is a subsequence of ", s, "." sep = '')
    else:
        print("The string \"", t, "\" is not a subsequence of ", s, "." sep = '')
    
def backwards(s):
    

def palindrome(s):
    

def subsequence(s, t):
    

main()