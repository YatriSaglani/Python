from Date_Time_Operations import Date_Time_Task
from file_operations import File_Operations_Task
from math_operations import Math_Operations_Task
from random_data import Random_Data_Task
from uuid_generator import UUID_Generator_Task

if __name__ == "__main__":

    while True:

        print("="*50 + "\nWelcome to the program...\n" + "="*50)

        print("1. Date & Time Operations")
        print("2. File Operations")
        print("3. Math Operations")
        print("4. Random Data")
        print("5. UUID Generator")
        print("6. Explore Module Attributes")
        print("7. Exit\n")
        
        choice = int(input("\nChoose an option : "))

        match choice:

            case 1:
                Date_Time_Task()

            case 2:
                File_Operations_Task()

            case 3:
                Math_Operations_Task()

            case 4:
                Random_Data_Task()

            case 5:
                UUID_Generator_Task()

            case 6:
                print(dir())

            case 7:
                print("="*50 + "\nExiting the program...\n" + "="*50)
                break
            case _:

                print("Invalid choice.")