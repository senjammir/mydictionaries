# Key has to be unique in a dictionary

person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# Print out the name of the spouse

print(person["spouse"])


# print out the name of the second child

print(person["children"][1])

# print out the name of the cat

print(person["pets"]["cat"])

# use a loop to print out the names of each child

for x in person["children"]:
    print(x)

# use a loop to print out the pets in the following format:
# the type of pet is: dog and the name of the pet is: Fido


for key, value in person["pets"].items():
    print(f"The type of the pet is: {key} and the name of the pet is: {value}")

# another method
# pet_dict = person["pets"]
# for key in pet_dict:
# print(f"the type of pet is: {key} and the name of the pet is: {pet_dict[key]}")

# .items will give you a tuple of the key and the value at the same time
