# quynh dao
# hey
def encode(input):
    result = ""
    tempnum = 0
    for i in range(0, len(input)):  # for loop i in the given input
        tempnum = int(input[i])
        result += str((tempnum + 3))  # each individual decimal added to the result to get the result
    return result

def decode():
    pass


if __name__ == "__main__":
    program = 1

    while program == 1:
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
            # “00009962” with become “33332295” after encoding.
            password_input = str(input("Please enter your password to encode: "))
            password_input = encode(password_input)




        elif menu_selection == 2: # subtracts 3 to each integer in the numeric string
            encoded_string = encode(numeric_input)
            print(f"The encoded password is {encoded_string}, and the original password is {numeric_input}.")


