# match.py
# Finds the minimum number of errors an amount of markers have compared to a protein
#
# Henry Lionni Guss
# 1/20/13

def main():
    inputFile = open("test.txt","r")
    protein = inputFile.readline()[:-1]
    nextLine = inputFile.readline()[:-1]
    sequence = 1
    #Loops through lines until there are no more
    while nextLine != "":
        best, errors = findBest(protein, nextLine)
        print("Sequence", sequence, "has", errors, "errors at position", best)
        nextLine = inputFile.readline()[:-1]
        sequence = sequence + 1

#This function finds the position with the least amount of errors matching a marker
def findBest(protein, marker):
    err = findAllErrors(protein, marker)
    best = 0
    #Loops through error values to find the position with the least errors
    for i in range(1,len(err)):
        best = findSmallest(best, err, i)
    return best, err[best]

#Returns the smallest of two values within a list
def findSmallest(best, err, i):
    if err[i] < err[best]:
        return i
    return best

#This function creates a list of the errors matching a marker at every position
def findAllErrors(protein, marker):
    err = [0] * (len(protein) - len(marker))
    #Loops through the positions of the protein, finding relative error counts
    for i in range(len(err)):
        err[i] = findPositionErrors(protein, marker, i)
    return err

#This function finds the errors matching a marker to a protein at a single position
def findPositionErrors(protein, marker, position):
    errors = 0
    #Loops through the marker, matching to a relative position of the protein
    for i in range(len(marker)):
        errors = checkMatch(position, i, marker, errors, protein)
    return errors

#This function determines returns a greater error value if two characters in don't match
def checkMatch(position, i, marker, errors, protein):
    if protein[i + position] != marker[i]:
        return errors + 1
    return errors

main()