

def print_pattern1():
    n = 5
    for i in range(1, n+1, 1):
        for j in range(1, i+1):
            print (j, end = ' ')
        print("")
    print ("")

print_pattern1() #function for pattern 1

def print_pattern2():
    n = 10
    for i in range(0, n+1):
        for j in range(n-i, 0, -1):
            print(j, end = ' ')
        print("")
    print("")

print_pattern2() #function for pattern 2

def search_prime_numbers():
    start = 10
    end = 50

    print(f'The prime numbers between {start} and {end} is:')
    for x in range(start, end+1):
        for y in range(2, x): #2 because everything modulus 1 == 0
            if x%y == 0:
                break #break loop if definite not prime

        else:
            print(x)
    print("")

search_prime_numbers() #function for search prime numbers between two points

def star_pattern():
    max = 5
    for x in range(1, max+1):
        for y in range(1, x+1):
            print("*", end = ' ') 
        print("")
    
    for x in range(1, max):
        for y in range(max-x, 0, -1):
            print("*", end = ' ')
        print("")

star_pattern() #function for star_pattern