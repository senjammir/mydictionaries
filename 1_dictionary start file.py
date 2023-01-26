import random

phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

# phonebook = {} ....this is an empty dictionary
# lists have elements and we can access the elements using indexing
# dictionaries have keys and values. e.g., Chris is the key and the number is the value in line 3
# Dicitonaries require the key and returns the value e.g., print(phonebook["Chris"])
"""

print()
print("*****  start section 1 - print dictionary ********")
print()

print(phonebook)

print(type(phonebook))  # type function returns the type of object we are dealing with
print(len(phonebook))  # prints the number of elements in the dictionary

mydictionary1 = dict(
    m=1,
    n=2,
)  # creates a dictionary

print(phonebook["Chris"])  # dictionaries are case sensitive


print()
print("*****  end section 1 ********")
print()


print()
print("*****  start section 2 - search dictionary ********")
print()

name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(f",{name} is not in the phone book")


print()
print("*****  end section 2 ********")
print()



print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)

phonebook["Chris"] = "555-01234"
phonebook["Joe"] = "555-4444"

print(phonebook)

print()
print("*****  end section 3 ********")
print()

print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

del phonebook["Chris"]  # deleting an element from dicitonary
print(phonebook)

print()
print("*****  end section 4 ********")
print()

print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()

for key in phonebook:
    print(key)  # print only keys through the for loop
    print(phonebook[key])  # print only values because we have the keys

for v in phonebook.values():  # only iterating through the values and not the key
    print(v)

mydict = {"mylist": [1, 2, 3, 4]}

for v in mydict.values(): #something wrong here?????
    for ele in v:
        print(type(ele))

for key, value in phonebook.items():
    print(f"Name: {key} and their phone number: {value}")

for ph_tuple in phonebook.items():
    print(type(ph_tuple)


print()
print("*****  end section 5 ********")
print()



print()
print("*****  start section 6 - using get and clear ********")
print()
"""

phone = phonebook.get("Chris", "key not found")
print(phone)

phonebook.clear()
print(phonebook)


print()
print("*****  end section 6 ********")
print()
"""

print()
print("*****  start section 7 - using pop method ********")
print()

remove = phonebook.pop("Chris","not found")
print(remove)
print(phonebook)


print()
print("*****  end section 7 ********")
print()


print()
print("*****  start section 8 - using popitem ********")
print()

a = phonebook.popitem() #its not random
print(a)
print(phonebook)


print()
print("*****  end section 8 ********")
print()


print()
print("*****  start section 9 - using random and converting to list ********")
print()
"""
list_of_keys = list(phonebook)
print(list_of_keys)

print(phonebook[random.choice(list_of_keys)])

print()
print("*****  end section 9 ********")
print()
