# Vishakh Surendran
def encoder(password):  # method to encode a password by adding three to each digit
    encoded_password = ""  # creates empty string to hold encoded password
    for i in password:  # iterates through password and adds 3 to each digit
        encoded_digit = (int(i) + 3) % 10
        encoded_password += str(encoded_digit)  # adds encoded digit to variable
    return encoded_password  # returns encoded password


def decoder(code):
    decoded_password = ""  
    for i in code:  # iterates through code and subtracts 3 to each digit
        decoded_digit = (int(i) - 3) % 10
        decoded_password += str(decoded_digit) 
    return decoded_password 


def main():  # main function
    continue_codec = True  # continues program
    encoded = None
    decoded = None
    while continue_codec:  # while loop to loop program
        print("Menu")  # prints menu with options for user
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        choice = int(input("Please enter an option: "))  # accepts int input for user choice
        if choice == 1:  # if choice is 1, encodes user provided password
            password = str(input("Please enter your password to encode: "))
            encoded = encoder(password)  # stores encoded password to variable
            print("Your password has been encoded and stored!\n")
        elif choice == 2:  # if choice is 2, decodes encoded password
            decoded = decoder(encoded)  # decodes encoded password and stores value
            print("The encoded password is " + encoded + " and the original password is " + decoded + ".\n")
            # prints statement with both encoded and original passwords
        elif choice == 3:  # if choice is 3, ends program
            continue_codec = False


if __name__ == "__main__":  # calls main function and executes program
    main()
# Done by: Sebastian Santa
