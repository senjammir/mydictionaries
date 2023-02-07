"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes



2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""
# 1 print out the number of earthquakes

import json

infile = open("eq_data.json", "r")
eq = json.load(infile)

count = len(eq["features"])

print("The number of Earthquakes recorded is", count, "\n")


# 2 Create new dictionary with eq above magnitude of 6

eq_dict = {}
list = []

for dict in eq["features"]:
    if dict["properties"]["mag"] > 6:
        new_dict = {}
        new_dict["Location"] = dict["properties"]["place"]
        new_dict["Magnitude"] = dict["properties"]["mag"]
        new_dict["Longitude"] = dict["geometry"]["coordinates"][0]
        new_dict["Latitude"] = dict["geometry"]["coordinates"][1]
        list.append(new_dict)

eq_dict["Earthquakes"] = list


# 3 Print out dictionary in desired format

x = 0
for i in eq_dict["Earthquakes"]:
    for key, value in i.items():
        print(f"{key} : {value}")
    if i != 0:
        print("\n\n")
    x += 1
