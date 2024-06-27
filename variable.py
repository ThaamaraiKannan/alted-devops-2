# var_1 = "10.75"
# print(var_1)
# print(type(var_1))

# var_2 = int(round(float(var_1)))
# print(var_2)
# print(type(var_2))
# list_example = ["Don't Know", "i know", "you know", "we know", "Don't Know"]
# tuple_example = ("Don't Know", "i know", "you know", "we know", "Don't Know")
# set_example = {"Don't Know", "i know", "you know", "we know", "Don't Know"}

# print(tuple_example)
# print(set_example[0])

# JSON -> JavaScript Object Notation
dict_example = {
    "glossary": {
        "title": 'example glossary',
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

print(type(dict_example["glossary"]["title"]))
print(dict_example["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["GlossDef"]["GlossSeeAlso"][1])
