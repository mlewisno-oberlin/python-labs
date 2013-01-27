# RecStr.py
# Learning to use recursion on strings.
# 
# Connor Davies
# 1/22/13

def main():
    print("Welcome to my Incredible Recursive String Thing!")
    print()
    
    s = input("Please enter a string:")
    t = input("Please enter another string:")
    print()
    
    print(s, "backwards is", rev(s))
    if pal(s):
        print("The String \"", s, "\" is a palindrome.", sep='')
    else:
        print("The String \"", s, "\" is not a palindrome.", sep='')
    if subseq(s, t):
        print("The String \"", t, "\" is a subsequence of \"", s, "\".", sep='')
    else:
        print("The String \"", t, "\" is not a subsequence of \"", s, "\".", sep='')
    print()
    
##
#Return string s reversed with recursion
#@param s The string too be reversed
#@return The reversed string of s
def rev(s):
    if len(s)==0: return ""
    return rev(s[1:len(s)])+s[0]

##
#Takes in a string s and checks to see if it is a pallindrome
#@param s The string to be checked for being a pallindrome
def pal(s):
    s2=rev(s)
    if s==s2: return True
    return False

##
#Takes in two strings and checks if the second is a subsequence of the first
#@param s The String that might contain the other.
#@param t The String being checked as a subsequence
#@return Returns True if t is a subsequence of s.
def subseq(s, t):
    if len(t)>len(s): return False
    if len(t)==0: return True
    if t[0]==s[0]: return subseq(s[1:len(s)],t[1:len(t)])
    return subseq(s[1:len(s)],t)

main()