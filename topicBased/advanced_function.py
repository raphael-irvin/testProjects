#Exercise 1 -> Return
def outer_func(a, b):
    square = a**2

    def inner_func(a, b):
        return square+b #return is used to return a value when called
    
    add = inner_func(a, b) #add will be assigned the returned value from inner_func
    return add+5 

result = outer_func(5, 5) #result will be assigned the returned value from outer_func
print(result)
print("")

def recursive_function(num):
    if num:
        return num + recursive_function(num-1)
    else:
        return 0

res = recursive_function(5)
print(res)