# Import necessary modules !
import random
import os
import clipboard

# For console color
os.system("cls")

# Create variables to store letters, digits, and punctuations
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = '0123456789'
punctuations = "@#$,!_"

# Create two functions, get_length() - to take length from user, generate_password() - to generate password !

# Convert List to String


def list2str(string):
    total = ""
    for i in string:
        total += i

    return total

# Take length of password from user !


def get_length():

    length = input("Choose length for your password : ")
    return int(length)

#


def get_choice():

    print('''What you want to remove :
                1 - Alphabets
                2 - Numbers
                3 - No change (Press any key to continue...)
            ''')

    choice = input()
    return choice


# Remove alphabets (Both:- capital and small)
def removealpha(password):
    for i in password:
        asciiVal = ord(i)
        if(asciiVal > 64 and asciiVal < 91) or (asciiVal > 96 and asciiVal < 123):
            password = password.replace(chr(asciiVal), "")

    return password

# Removes numbers


def removeNumbers(password):
    for i in password:
        asciiVal = ord(i)
        if(asciiVal > 47 and asciiVal < 58):
            password = password.replace(chr(asciiVal), "")

    return password


# Main password generation !


def generate_password(length, choice):

    password = f'{letters}{digits}{punctuations}'
    result = ""

    if choice == "1":
        result = removealpha(password)
    elif choice == "2":
        result = removeNumbers(password)
    else:
        result = password

    # Convert password to list

    password = list(result)

    # Randomly shuffle this password !

    random.shuffle(password)

    # Pick random combination from this shuffled list !

    random_password = random.choices(password, k=length)

    # Convert List to String
    final_password = list2str(random_password)

    return final_password


# Driver Code
if __name__ == '__main__':
    condition = True
    while condition:

        # Ask user to get length of password !
        length = get_length()
        choice = get_choice()
        password = generate_password(length, choice)

        # Print password !
        print("Password - ", end="")
        print(f"\033[42m{password}\033[00m")

        clipboard.copy(password)
        print()
        print("\033[45mCopied to clipboard !\033[00m")

        # Condition to break the loop !
        print('''Options :
                1 - Suggest another password
                2 - Exit
                ''')
        condition = input()
        if condition == "2":
            condition = False


for i in range(0, 50):
    print("\033[93m -\033[00m", end="")
print()
