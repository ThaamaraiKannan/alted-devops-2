def print_function(value):
    print(value)

def marks_check(mark):
    if mark > 35:
         print_function("Pass")
         print_function("Fail")
    else:
         print_function("Fail")


marks_check(25)
marks_check(125)
marks_check(10)
marks_check(8)
marks_check(95)
marks_check(75)