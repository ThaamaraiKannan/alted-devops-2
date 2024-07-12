
def marks_check(mark):
    if mark > 35:
        return "pass"
    else:
        return "fail"


def print_function(value):
    print(value)



print_function(marks_check(25))
print_function(marks_check(125))
print_function(marks_check(10))
print_function(marks_check(8))
print_function(marks_check(95))
print_function(marks_check(75))
