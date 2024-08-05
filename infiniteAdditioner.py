import numpy

global userNumberCol
userNumberCol = []

def NumberSystem():
    global userNumber

    userNumber = 0

    def inputNumber():
        global userNumber
        while userNumber != "DONE":
            userNumber = input("Please input the numbers, write 'DONE' when you are finished: ")

            try:
                userNumber = int(userNumber)
                print("Number succesfully registered!")
                userNumberCol.append(userNumber)
                print ("Your current numbers are:")
                print (userNumberCol)

            except ValueError: 
                userNumber = str.upper(userNumber)
        
        def runResult():
            global userNumberCol
            result = sum(userNumberCol)
            return result

        finalResult = runResult()

        print("THE FINAL RESULTS ARE")
        print(finalResult)

    inputNumber()


NumberSystem()
