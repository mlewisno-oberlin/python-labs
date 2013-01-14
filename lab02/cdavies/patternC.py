# patternC.py
# Makes a pattern
# 
# Connor Davies
# 1/9/13

def main():
    n = eval(input("Please enter a number:"))
    for i in range(0,n):
        for j in range(i,n):
            print(j+1, "", end="")
        print()
main()