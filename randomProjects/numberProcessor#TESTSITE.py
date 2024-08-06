import random
numList = []
def numGen():
    global numList
    i = 0
    while i != 100:
        num = random.randrange(1, 10000)
        numList.append(num)
        i += 1
    
    print ("")
    print ("THE NUMBERS ARE")
    print (numList)

def main():
    global numList
    numAcum = []
    limitor = len(numList)
    phase = 0
    for x in numList:
        print ("")
        print ("CURRENT PHASE: " + str(phase))
        numAcum1 = 0
        numAcumSub = []
        curCheck = 0
        while curCheck != limitor:
            numAcum1 = x + numList[curCheck]
            numAcumSub.append(numAcum1)
            curCheck += 1

        i = 0
        for x in numAcumSub:
            numAcum.append(numAcumSub[i])
            i += 1

        phase += 1

    #SWEEPER
    numAcumFiltered = list(dict.fromkeys(numAcum))

    print ("")
    print ("CLEANING PROCESS FINISHED, FINAL LIST:")
    print (numAcumFiltered)
    print ("")
    filterAscending = input("Do you want to filter ascendingly? (YES/NO): ")
    if filterAscending == "YES":
        numAcumFiltered.sort()
        print ("")
        print ("SORTING COMPLETE!")
        print (numAcumFiltered)
        

numGen()
main()