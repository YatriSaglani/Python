while True:

    print("\nWelcome to Pattern Generator and Number Analyzer\n")

    print("Select an option from list provided below")
    print("1.Generate a pattern")
    print("2.Analyze a range of numbers")
    print("3.Exit")

    choice = int(input("\nEnter your choice : "))

    match choice:

        case 1:
            print("\nYou chose to Generate a Pattern so please choose what do you want to print in pattern")
            print("1. * ")
            print("2. # ")
            print("3. $ ")
            print("4. Numbers ")

            choose = int(input("\nEnter Your Choice : "))

            match choose:

                case 1:
                    rows = int(input("Enter the number of rows : "))
                    for i in range(1, rows + 1):
                        print(" * " * i)

                case 2:
                    rows = int(input("Enter the number of rows : "))
                    for i in range(1, rows + 1):
                        print(" # " * i)

                case 3:
                    rows = int(input("Enter the number of rows : "))
                    for i in range(1, rows + 1):
                        print(" $ " * i)

                case 4:
                    rows = int(input("Enter the number of rows : "))
                    for i in range(1, rows + 1):
                        for j in range(1, i + 1):
                            print(j, end=" ")
                        print()

                case _:
                    print("Invalid Pattern Choice!")

        case 2:
            print("\nYou chose to Analyze a range of numbers\n")

            start = int(input("Enter the start of the range : "))
            end = int(input("Enter the end of the range : "))

            total = 0

            for i in range(start, end + 1):
                total += i

                if i % 2 == 0:
                    print("Number", i, "is even")
                else:
                    print("Number", i, "is odd")

            print("\nSum of all numbers is :", total)

        case 3:
            print("\nExiting the Program, Goodbye!!!")
            break

        case _:
            print("\nSorry! You entered an invalid choice!")