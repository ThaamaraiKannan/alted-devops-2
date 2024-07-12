# try:
#     def main(num1, num2):
#         result = num1/num2
#         print(result)
#         return

#     main(10, 0)
# except Exception as err:
#     print(err)


def main(num1, num2):
    try:
        result = num1/num2
        print(result)
        return
    except ZeroDivisionError:
        print("dicided by zero")
    except Exception as err:
        print("error >>>>>>", err)

main(10, 0)