# patternE.py
# Makes a pattern
# 
# Connor Davies
# 1/9/13

def main():
    n = eval(input("Please enter a number:"))
    for i in range(0,3+(n*2)):
        print("*", end="")
        if(i==0):
            for j in range(0, n+1):
                print("*", end="")
        if(i==((3+(n*2))//2)):
            for j in range(0, n):
                print("*", end="")
        if(i==3+(n*2)-1):
            for j in range(0, n+1):
                print("*", end="")
        print()
main()