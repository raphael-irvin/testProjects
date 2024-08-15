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
thisdict4["color"] = "white" #this formula can be used to add a new key:value pair
print(thisdict4)