#module
import random
import os

#gameMainSystem
gameScore = 0

#pre-def
divider = "-------------------------------------------"

def gameSys():
    global gameScore
    global setScore
    setScore = 0
    global betRisk
    betRisk = 0
    global currentNum
    currentNum = []
    os.system('CLS')

    print (divider)
    print ("WELCOME TO THE BET GAME!")
    print ("HOW TO PLAY:")
    print ("You will be asked to pick an amount of randomized number from 1-10 to generate.")
    print ("")
    print ("Scoring System:")
    print ("Sum of numbers is below 10 | 10 POINTS FOR EACH GENERATED NUMBER")
    print ("Sum of numbers is below 25 | 5 POINTS FOR EACH GENERATED NUMBER")
    print ("Sum of numbers is below 50 | 2 POINTS FOR EACH GENERATED NUMBER")
    print ("Sum of numbers is above 50 | GAME OVER!")
    print ("")
    print (divider)

    def numGenerator():
        global currentNum
        global betRisk
        betRisk = input("How many numbers would you like to generate: ")
        betRisk = int(betRisk)
        i = 0
        while i != betRisk:
            numGen = random.randrange(1,10)
            currentNum.append(numGen)
            i += 1
    
    def calcSet():
        global currentNum
        global setScore
        print (currentNum)
        setSum = sum(currentNum)
        print ("Your sum is: " + str(setSum))
        print ("")

        if setSum <= 10:
            print ("Congratulations for getting below 10!")
            setScore = 10*betRisk
            print ("Points gained: 10 x " + str(betRisk) + " numbers generated = " + str(setScore) + "Pts")
        
        elif setSum <= 25:
            print ("Congratulations for getting below 25!")
            setScore = 5*betRisk
            print ("Points gained: 5 x " + str(betRisk) + " numbers generated = " + str(setScore) + "Pts")

        elif setSum <= 50:
            print ("Congratulations for getting below 50!")
            setScore = 2*betRisk
            print ("Points gained: 2 x " + str(betRisk) + " numbers generated = " + str(setScore) + "Pts")

        else:
            print ("Oops! Threshold Reached!")
        
    def resultScreen():
        print ("")
        global gameScore
        global setScore
        global userTry
        gameScore += setScore
        print ("Your Current Game Score is: " + str(gameScore))
        userTry = "x"
        def userTryAgain():
            global userTry
            userTry = input ("Do you want to continue? (YES/NO)")
            userTry = userTry.upper()
            if userTry == "YES":
                gameSys()
            elif userTry == "NO":
                print ("Thank you for playing!")
            else:
                print("Selection unrecognized, please try again!")
                userTryAgain()
        
        userTryAgain()

    
    numGenerator()
    calcSet()
    resultScreen()


gameSys()


