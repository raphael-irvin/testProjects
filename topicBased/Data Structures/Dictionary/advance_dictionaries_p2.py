#SOURCE: https://pynative.com/python-dictionary-exercise-with-solutions/ 
#--------------------------------------------------------------------------

#EXERCISE 1 -> Making a dictionary from 2 lists (1 for key, 1 for value)
keys = ["key 1", "key 2", "key 3"]
values = ["value 1", "value 2", "value 3"]

res_dict = dict(zip(keys, values))
print(res_dict)
print("")

#-------------------------------------------------------------------------

#EXERCISE 2 -> MERGING TWO DICTIONARIES TO ONE
dict1 = {"one":1, "two":2, "three":3}
dict2 = {"four":4, "five":5, "six":6}

#METHOD 1
dict3 = {**dict1, **dict2} #with ** symbol
print(dict3)

#METHOD 2
dict3 = dict1.copy() #Copy dict1 to dict3
dict3.update(dict2) #Update (add) the list of dict2 to dict3
print(dict3)
print("")

#-------------------------------------------------------------------------

#EXERCISE 5 -> CREATE A DICTIONARY FROM A SPECIFIC KEY/VALUE PAIR OF A DICT
sample_dict = {
    "name": "johny",
    "age": 20,
    "salary": 3000,
    "city": "Jakarta"
}

#Keys we want to extract
keys = ["name", "age"]

new_dict = {k: sample_dict[k] for k in keys} #This is dictionary comprehension
print(new_dict)