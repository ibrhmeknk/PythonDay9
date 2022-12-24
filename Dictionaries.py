programming_dictionary = {"Bug": "Error", "Function": "A piece of code"}

print(programming_dictionary["Function"])

programming_dictionary["Function"] = "How to edit a dictionary."

print(programming_dictionary["Function"])

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])