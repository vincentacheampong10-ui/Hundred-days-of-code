programming_dictionary = {
    "Bug": "An error is a program that prevents the program from working correctly",
     "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again"
}


print(programming_dictionary["Bug"])

# Add to an existing dictionary
programming_dictionary["loops"] = "The action of doing something over and over again"
print(programming_dictionary)

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nested lists in Dictionary

# travel_log = {
#     "France": ["Paris", "lille", "Dijon"],
#     "Germany": ["Stuttgart" , "Berlin"]
# }

# print(travel_log["France"][0])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "lille", "Dijon" ],
        "total_visits": 12
    },
    "Germany":{
        "cities_visited": ["Stuttgart" , "Berlin"],
        "total_visits": 12
    },
}

print(travel_log["Germany"]["cities_visited"][1])