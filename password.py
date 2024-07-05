
### number = 0

def checkdigits(val, digit):
    try:
        if val == 0 :
            return "None"
        total = 0
        while val > 0:
            val //=digit
            total += 1
        return total
    except Exception as error:
        print(error)
        

def addition(num1, num2, digit = 10):
    try:
        num1_digit = checkdigits(num1, digit)
        num2_digit = checkdigits(num2, digit)
        if num1_digit > digit or num2_digit > digit:
            print("not authorize to perform")
            return
        else:
            return print(num1 + num2)
    except Exception as value:
        print(value)

addition(123456789000111, 1234669, 12)
addition(1234567890, 1234669, 0)
addition(1256, 1234669)
addition(1256, 9876543)

