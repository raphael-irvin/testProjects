#SOURCE: https://www.w3schools.com/python/python_dictionaries_loop.asp 

thisdict = dict(brand = "Hyundai", model = "Stargazer", year = 2003) #make a dict using constructor


#SECTION 1: LOOPING DICTIONARY -----------------------------------------------------
for x in thisdict: #this will print all "keys" of a dictionary
    print(x)
print("")

for x in thisdict: #this will print all "value" of a dictionary
    print (thisdict[x])
print("")


#SECTION 2 -----------------------------------------------------

#METHOD 1
for x in thisdict:
    print(f'{x}: {thisdict[x]}')

print("")

#METHOD 2
for x,y in thisdict.items():
    print(f'{x}: {y}')


#SECTION 3: NESTED DICTIONARY -----------------------------------------------------
parentdict = {
    "childdict1": {
        "name": "child1",
        "id": 1
    },
    "childdict2": {
        "name": "child2",
        "id": 2
    },
    "childdict3": {
        "name": "child3",
        "id": 3
    }
}

#OR

childdict1_1 = {
        "name": "child1",
        "id": 1
}
childdict2_1 = {
        "name": "child2",
        "id": 2
}
childdict3_1 = {
        "name": "child3",
        "id": 3
}

#then assign a dictionary that contains the three dict
parentdict2 = {
    "childdict1_1": childdict1_1,
    "childdict2_1": childdict2_1,
    "childdict3_1": childdict3_1
}

#accessing nested dictionary items
print(parentdict["childdict1"]["name"])
print("")

#looping through all keys and values of nested dictionary
for x, y in parentdict.items():
    print(x)

    for z in y:
        print (f'{z}: {y[z]}')
    print("")