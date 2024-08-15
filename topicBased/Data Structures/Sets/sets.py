'''
A set is an IMMUTABLE, UNORDERED collection of UNIQUE (cannot duplicate) elements,
 that CAN consist of integers, floats, strings and tuples. 
 However, sets CANNOT hold mutable elements such as 
 lists, sets or dictionaries.
'''


#A set is created using {}
set1 = {10.5, "abc", 20, "cba"}
print (f'the type is {type(set1)}, the value is {set1}')
print("")


#A set can be created from a list
list1 = [10.5, "john", "john", 20]
set1 = set(list1) #List duplicates removed!
print(set1)
print("")


#Accessing and Writing in Sets
names = {"john", "george", "jason", "budi"}
print ("john" in names) #can be accessed with "in", output: True
names.add("Niko") #adds a new elements
print(names)
#EXISTING ELEMENTS ARE IMMUTABLE (CANNOT BE CHANGED), BUT NEW ELEMENTS CAN BE ADDED
print("")


#Joining/Removing
students1 = {"junior", "alpha", "beta"}
students2 = {"charlie", "delta", "echo"}
students1.update(students2) #using update()
print (students1)

students3 = students1.union(students2) #using union()
print(students3)

students3.remove("junior") #remove() removes the specified item
print(students3)
print("")