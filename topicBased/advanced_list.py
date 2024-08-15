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

change_all_type = ["hello" for x in new_list]
print(change_all_type)

change_all_type_else = ["under 5" if x<5 else "above 5" for x in new_list]
print(change_all_type_else)