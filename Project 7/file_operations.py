def File_Operations_Task():

    while True:
        print("\n1.create a new file")
        print("2.write to a file")
        print("3.read from a file")
        print("4.append to a file")
        print("5.back to main menu")

        choice = int(input("Choose an option : "))

        match choice:

            case 1:
                file_name = input("Enter file name: ")
                file = open(file_name, "w")
                file.close()
                print("File created successfully.")

            case 2:
                file = open("D:\\Python\\Project 7\\FileOperations.txt", "w")
                content = input("Enter the content to write to the file: ")
                file.write(content)
                file.close()
                print("Content written successfully.")

            case 3:
                file = open("D:\\Python\\Project 7\\FileOperations.txt", "r")
                content = file.read()
                print("Content of the file:")
                print(content)
                file.close()

            case 4:
                file = open("D:\\Python\\Project 7\\FileOperations.txt", "a")
                content = input("Enter the content to append to the file: ")
                file.write(content)
                file.close()
                print("Content appended successfully.")

            case 5:
                print("Returning to main menu...")
                break


if __name__ == "__main__":
    File_Operations_Task()