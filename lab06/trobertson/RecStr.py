# recStr.py
# gives various feedback on two user inputed strings
#
# Tyler Robertson
# 1/25/13

def main() :
    s = input("Please enter string s: ")
    t = input("Please enter string t: ")
    print("\nThe String \"",s,"\" backwards is \"",backwards(s),"\".",sep='')
    if pal(s) : print("The String \"",s,"\" is a palindrome.",sep='')
    else : print("The String \"",s,"\" is not a palindrome.",sep='')
    if sub(t,s) : print("The String \"",t,"\" is a subsequence of \"",s,"\".",sep='')
    else : print("The String \"",t,"\" is not a subsequence of \"",s,"\".",sep='')
    
# Returns a happy little string of the user's input read backwards!
def backwards(s) :
    if len(s) == 0 :
        return s
    else:
        return s[len(s)-1] + backwards(s[:-1])

# Tells the user if their input is a palindrome
def pal(s) :
    if len(s) == 0 :
        return True
    if len(s) == 1 :
        return True
    else:
        if s[0] != s[len(s)-1] :
            return False
        else:
            return pal(s[1:len(s)-1])
    
# Tells the user if t is a substring of s
def sub(t,s) :
    if len(t) == 0 :
        return True
    if len(t) > len(s) :
        return False
    if s[0] == t[0] :
        return sub(t[1:],s[1:])
    else :
        return sub(t[1:],s)
    
main()
