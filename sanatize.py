def sanitize_int(message, minimum, maximum):
    number = 0
    while True:
        try:
            number = int(input(message))
            if maximum >= number >= minimum:
                break
            else:
                print("Invalid entry, the maximum you can have is {} and the minimum is {}.".format(maximum, minimum))
        except ValueError as e:
            print("Invalid entry the entry must be an integer")
            print(e)
    return number