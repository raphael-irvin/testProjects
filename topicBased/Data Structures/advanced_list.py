#--------------- LIST COMPREHENSION ----------------------
#SOURCE: https://www.w3schools.com/python/python_lists_comprehension.asp 

#--------------- EXAMPLE 1 -------------------

#Default
default_new_list = []
for x in range(11):
    default_new_list.append(x)
print(default_new_list)
print("")

#List Comprehension
new_list = [x for x in range(11)]
print(new_list)
print("")

#--------------- EXAMPLE 2 -------------------
odd_list = [x for x in new_list if x%2 != 0]
print(odd_list)

even_list = [x for x in new_list if x%2 == 0]
print(even_list)
print("")

change_all_type = ["hello" for x in new_list]
print(change_all_type)

change_all_type_else = ["under 5" if x<5 else "above 5" for x in new_list]
print(change_all_type_else)

#----------------------------------------------------------

#--------------- ADVANCED LIST ----------------------
#SOURCE
#https://pynative.com/python-data-structure-exercise-for-beginners/ 

#TOPIC: List start:stop:step
def advanced_list1():
    list = ["a","b","c","d","e","f","g","h"]
    odd_list = list[1::2] #start at index 1, stop at max, step 2
    even_list = list[0::2] #start at index 0, stop at max, step 2
    print(f'Elements with odd index: {odd_list}')
    print(f'Elements with even index: {even_list}')

def another_example():
    list = [0,1,2,3,4,5,6,7,8,9,10]
    chosen_list = list[0:6:1] #start at index 0, stop at index 6, step 1
    print(f'Elements with index 0-6: {chosen_list}')

advanced_list1()
print("")
another_example()
print("")

#From Exercise 2 -> TOPIC: Pop() and Insert()
def exercise2():
    list = [0,1,2,3,4,5,6,7,8,9,10]
    print(f'Original List: {list}')
    taken_number = list.pop(3) #pop removes the item from the list and return the value
    print(f'Value of taken_number after popping index 3: {taken_number}')
    print(f'List after index 3 popped: {list}')
    list.insert(0, taken_number) #insert (index, item)
    print(f'List after popped item inserted at index 0: {list}')

exercise2()
print("")