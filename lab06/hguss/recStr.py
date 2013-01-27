# recStr.py
# Performs recursive string operations
#
# Henry Lionni Guss
# 1/26/13

def main():
    #Print Directions
    print("This program will print a string backwards, determine whether or not it",
        "is a palindrome, and determine whether or not a second string is within it.")
    #Receive input strings
    s = input("Enter a first string (to perform backwards and palindrome): ")
    t = input("Enter a second string to find within the first: ")
    print("The string \"", s, "\" backwards is ", backwards(s), ".", sep = '')
    #Determines and prints whether s is a palindrome
    if palindrome(s) == True:
        print("The string \"", s, "\" is a palindrome.", sep = '')
    else:
        print("The string \"", s, "\" is not a palindrome.", sep = '')
    #Determines and prints whether t is a subsequence of s
    if subsequence(s, t) == True:
        print("The string \"", t, "\" is a subsequence of ", s, ".", sep = '')
    else:
        print("The string \"", t, "\" is not a subsequence of ", s, ".", sep = '')
    
def backwards(s):
    #Base case where s is an empty string
    if s == "":
        return s
    #Returns last character plus the rest of the string backwards
    return s[-1] + backwards(s[:-1])

def palindrome(s):
    #A single character or empty string is always a palindrome
    if s == "" or len(s) == 1:
        return True
    #If the first and last characters are not the same, the string is not a palindrome
    if s[-1] != s[0]:
        return False
    #A string with identical first and last characters is a palindrome if the inside is
    #a palindrome as well
    return palindrome(s[1:-1])

def subsequence(s, t):
    #An empty string can always be found in any other string
    if t == "":
        return True
    #A string cannot be a subsequence of a shorter string
    if len(t) > len(s):
        return False
    #If the first characters match, the rest of the subsequence must be present
    #within the rest of the larger string
    if t[0] == s[0]:
        return subsequence(s[1:], t[1:])
    #If the the subsequence cannot be found immediately, it might be found later
    return subsequence(s[1:], t)

main()