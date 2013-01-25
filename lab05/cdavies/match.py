# match.py
# Finds the best matching of two protein sequences
# 
# Connor Davies
# 1/15/13

def main():
    inputFile = open("test.txt", "r")
    code = inputFile.readline()
    i = 1
    for line in inputFile:
        line=line[0:len(line)-1]
        minimum, position = match(code, line)
        print("Sequence ", i, " has ", minimum, " errors at position ", position, ".", sep='')
        i=i+1
        
        
def match(code, line):
    maximum = 0
    position = 0
    current = 0
    for i in range(0,len(code)-len(line)+1):
        for j in range(i,len(line)+i):
            if code[j]==line[j-i]:
                current=current+1
        if current>maximum:
            maximum=current
            position = i
        current=0
    return len(line)-maximum, position
        

main()
    