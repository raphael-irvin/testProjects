#Dictionaries are made out of key:value pairs
thisdict = {
    "brand": "honda",
    "model": "brio",
    "year" : 2003
}

print(thisdict)
print (thisdict["brand"])
print("")

thisdict2 = {
    "brand": "honda",
    "model": "brio",
    "year" : 2003,
    "year" : 2004 #Dictionary cannot be duplicate, duplicate will overwrite existing ones
}

print(thisdict2["year"])
print("")

thisdict3 = { #Dictionaries can hold multiple data types/structures at once
    "brand": "honda",
    "year": 2003,
    "electric": False,
    "color": ["red", "white", "blue"]
}

#this is a dictionary constructor -> dictionary_name = dict(key:value, ....)
thisdict4 = dict(brand = "honda", year = 2003, electric = False)
print(thisdict4)
print(thisdict4.keys()) #dictionaryname.keys() is used to get the list of keys in a dictionary
print(thisdict4.values()) #dictionaryname.values() is used to get the list of values in a dictionary

print("")
thisdict4["color"] = "white" #this formula can be used to add/change a key:value pair
thisdict4.update({"color": "white"}) #or use thisdict4.update({key:value})
print(thisdict4)

print("")
thisdict5 = dict(brand = "honda", year = 2003, electric = False)
thisdict5.pop("brand") #dictionaryname.pop("key") can be used to remove a key:value pair in a dict
thisdict5.popitem() #dictionaryname.popitem() can be used to remove the LAST key:value pair in a dict
del thisdict5["year"] #del dictionaryname["key"] can also be used to remove a key:value pair in a dict
print(thisdict5)

thisdict5 = dict(brand = "honda", year = 2003, electric = False)
thisdict5.clear() #this can be used to clear/empty a dictionary
print(thisdict5)