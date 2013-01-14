# patternN.py
# Makes a pattern
# 
# Connor Davies
# 1/9/13

def main():
    n = eval(input("Please enter a number:"))
    print("*", end="")
    for i in range(0,n+1):
        print(" ", end="")
    print("*")
    
    for i in range(0,n+1):
        print("*", end="")
        for j in range(0,n+1):
            if(j==i):
                print("*", end="")
            else:
                print(" ", end="")
        print("*")
    
    print("*", end="")
    for i in range(0,n+1):
        print(" ", end="")
    print("*")
    
main()