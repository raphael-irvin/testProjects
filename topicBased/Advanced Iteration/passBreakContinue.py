def passFunc():
    i = 0
    while i <= 10:
        if i%2 == 0:
            print (i)
        else:
            pass #-> Pass = Do Nothing, Continue the rest of the loop
        print (f'NUMBER {i} IS PROCESSED!')
        i += 1

def breakFunc():
    i = 0
    while i <= 10:
        if i%2 == 0:
            print (i)
        else:
            break #-> Break = STOP THE LOOP!
        print (f'NUMBER {i} IS PROCESSED!')
        i += 1

def continueFunc():
    i = 0
    while i <= 10:
        if i%2 == 0:
            print (i)
        else:
            continue #-> Continue = Skip the rest of the loop, immediately start the loop from top!
        print (f'NUMBER {i} IS PROCESSED!')
        i += 1

print ("THIS IS PASS")
passFunc()

print ("")

print ("THIS IS BREAK")
breakFunc()

print ("")

print ("THIS IS CONTINUE")
continueFunc()