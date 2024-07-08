
import re
sample_string = """Kannan@ 123"""

# print(sample_string.replace("to", "kannan"))

regex = r"^(?=.+[A-Za-z])(?=.+\d)(?=.+\s)(?=.+[@$!%*])[A-Za-z\d\s@$!%*]{8,}$"
compl = 10+10j
print(re.match(regex, sample_string))