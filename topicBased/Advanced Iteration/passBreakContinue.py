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
            i+=1
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

def pass_break_continue_quiz():
    numbers = [12, 75, 150, 180, 145, 525, 50]
    #Harus bisa dibagi 5
    #Kalo lebih besar dari 150, skip, move to next number
    #Kalo lebih dari 500, stop the loop

    for x in numbers:
        if x%5 == 0:
            if x > 500:
                break
            elif x > 150:
                continue
            else:
                print(x)

        else:
            pass

pass_break_continue_quiz()