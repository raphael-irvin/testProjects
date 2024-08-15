#SOURCE
#https://pynative.com/python-functions-exercise-with-solutions/

#From Exercise 5 -> Topic: Return
def outer_func(a, b):
    square = a**2

    def inner_func(a, b):
        return square+b #return is used to return a value when called
    
    add = inner_func(a, b) #add will be assigned the returned value from inner_func 
    return add+5

result = outer_func(5, 5) #result will be assigned the returned value from outer_func
print(result)
print("")

#From Exercise 6 -> Topic: Recursive Function
def recursive_function(number):
    if number:
        return number + recursive_function(number-1) #this is recursive function; return calling function
    else:
        return 0

res = recursive_function(5)
print(res)
print("")

