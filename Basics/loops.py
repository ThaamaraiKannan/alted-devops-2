
# example_list  = {
#    "ID": "SGML",
# 					"SortAs": "SGML",
# 					"GlossTerm": "Standard Generalized Markup Language",
# 					"Acronym": "SGML",
# 					"Abbrev": "ISO 8879:1986",
# 					"GlossDef": {
#                         "para": "A meta-markup language, used to create markup languages such as DocBook.",
# 						"GlossSeeAlso": ["GML", "XML"]
#                     },
# 					"GlossSee": "markup"
# }

# print(type(example_list))
# example_list["ID"]
# example_list["SortAs"]
# example_list["GlossTerm"]


# for data in example_list:
#     print(example_list[data])


number = int(input('Enter a number: '))
total = 0
# iterate until the user enters 0
while number != 0:
    total +=  number
    number = int(input('Enter a number: '))
print('The sum is', total)










