def print_func(value):
    print(value)
    return

def calc(a, b , c):
    try:
        if c == "add" or c == "+":
            return int(a) + int(b)
        elif c == "sub" or c == "-":
            return int(a) - int(b)
        elif c == "mul" or c == "*":
            return int(a) * int(b)
        elif c == "div" or c == "/":
            return int(a) / int(b)
    except Exception as err:
        return f"There is an error >>>>> , {err}"