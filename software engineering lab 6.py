# quynh dao

def encode(input):
    result = ""
    for num in input:  # for loop i in the given input
           num += 3# i put through decimal to hex method
        result.append(num)  # each individual decimal added to the result to get the result
    return result

def decode():
    pass


if __name__ == "__main__":
    program = 1

    while program != 1:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        menu_selection = int(input("Please enter an option: "))


        if menu_selection == 3:
            break

        elif menu_selection == 1: # adds 3 to each integer in the numeric string
            # “12345555” will become “45678888” after encoding.
            # “00009962” will become “33332295” after encoding.
            password_input = int(input("Please enter your password to encode:"))



        elif menu_selection == 2: # subtracts 3 to each integer in the numeric string
            encoded_string = encode(numeric_input)
            print(f"The encoded password is {encoded_string}, and the original password is {numeric_input}.")


