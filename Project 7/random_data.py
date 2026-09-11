import random
import string


def Random_Data_Task():

    while True:
        print("\n1.Generate random integer")
        print("2.Generate random list")
        print("3.create random password")
        print("4.Generate random OTP")
        print("5.Back to main menu\n")

        choice = int(input("Choose an option : "))

        match choice:

            case 1:
                lower = int(input("Enter the lower bound: "))
                upper = int(input("Enter the upper bound: "))

                random_integer = random.randint(lower, upper)

                print("Random Integer:", random_integer)

            case 2:
                size = int(input("Enter the size of the list: "))
                lower = int(input("Enter the lower bound for list elements: "))
                upper = int(input("Enter the upper bound for list elements: "))

                random_list = [
                    random.randint(lower, upper)
                    for _ in range(size)
                ]

                print("Random List:", random_list)

            case 3:
                length = int(input("Enter the desired password length: "))

                characters = string.ascii_letters + string.digits + string.punctuation

                password = ''.join(
                    random.choice(characters)
                    for _ in range(length)
                )

                print("Random Password:", password)

            case 4:
                otp_length = int(input("Enter the desired OTP length: "))

                otp = ''.join(
                    random.choices(string.digits, k=otp_length)
                )

                print("Random OTP:", otp)

            case 5:
                print("Returning to main menu...")
                break


if __name__ == "__main__":
    Random_Data_Task()