def valid_func(ip, value = True, kannan = "nothing given"):
    print(ip)
    print(value)
    print(kannan)
    try:
        number = ip.split(".")
        valid = False
        try:
            for data in number:
                # 192
                verify_num = int(data)
                if verify_num >= 0 and verify_num <= 255:
                    valid = True
                else:
                    valid = False   
                    break
        except Exception as err:
            print(err)
        if valid == True:
            print("Valid IP\n")
        elif valid == False:
            print("Invalid IP\n")
        return
    except AttributeError as error:
        print(error)
        print("give the argument Like this eg: 10.1.100.89")

try:
    valid_func("10.1.100.89", 10, 100)
    valid_func("55.65.23.125")
    valid_func("452.326.123.12")
    valid_func("152.896.255.255")
except Exception as error:
    print(error)