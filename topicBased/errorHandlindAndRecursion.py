def main():

    def numSys(x):
        if x == 1:
            print("BASELINE (1) REACHED!")
            return 1
        else:
            return x * numSys(x-1)

    def userSystem():
        a = input("Initial Number: ")
        try:
            a = int(a)
            return a
        except:
            print("ERROR! Please type a valid number!")
            return userSystem()
    
    #FLOW
    factorialSum = numSys(userSystem())
    print(factorialSum)

main()