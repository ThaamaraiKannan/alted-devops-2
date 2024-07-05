from main import print_func, calc

def my_func():
    try:
        response = calc("2",3, "*")
        print_func(response)
    except AttributeError:
        print(AttributeError)

my_func()