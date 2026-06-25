print("Welcome to Student Data Analyzer and Transformer Program")

li = []

def takeInput():
    global li
    li=[int(i) for i in input("\nEnter ellement seperated by space : ").split(" ")]

    print("\nElements Inserted Successfully!")

def displaySummary(*args):
    """
    Displays basic statistics of the dataset using built-in functions.
    """
    data = args[0]

    largest = max(data)
    smallest = min(data)
    average = sum(data) / len(data)

    print("\nData Summary:")
    print("Length of list:", len(data))
    print("Minimum Value:", smallest)
    print("Maximum Value:", largest)
    print("Sum of all Values:", sum(data))
    print("Average Value:", round(average, 2))

def factorial(num):
    """
    Calculates factorial using recursion.
    """
    if num <= 1:
        return 1
    return num * factorial(num - 1)

def threshold():
    """
    Filters values above the threshold using lambda and filter.
    """
    value = int(input("Enter a value to filter out data above this value: "))
    result = list(filter(lambda x: x > value, li))
    return result

def sorting():
    """
    Sorts the list in ascending or descending order.
    """
    print("\n1. Ascending")
    print("2. Descending")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sorted_list = sorted(li)
    elif choice == 2:
        sorted_list = sorted(li, reverse=True)
    else:
        print("Invalid Choice!")
        return

    print("Sorted List:", sorted_list)

def dataset_statistics(data):
    """
    Returns minimum, maximum, total and average.
    """
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)

    return minimum, maximum, total, average

def show_info(**kwargs):
    """
    Displays information using keyword arguments.
    """
    print("\nProgram Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

while True:

    print("\n========== MAIN MENU ==========")
    print("1.Input Data")
    print("2.Display Data Summary (Built-in Functions)")
    print("3.Calculate Factorial (Recursion)")
    print("4.Filter Data by Threshold (Lambda Function)")
    print("5.Sort Data")
    print("6.Display Dataset Statistics (Return Multiple Values)")
    print("7.Show Program Information (kwargs)")
    print("8.Exit")

    choice = int(input("\nPlease Enter Your Choice: "))

    match choice:

        case 1:
            takeInput()

        case 2:
            if len(li) == 0:
                print("Please enter data first!")
            else:
                displaySummary(li)

        case 3:
            num = int(input("Enter a number: "))
            print("Factorial =", factorial(num))

        case 4:
            if len(li) == 0:
                print("Please enter data first!")
            else:
                result = threshold()
                print("Filtered Data:", result)

        case 5:
            if len(li) == 0:
                print("Please enter data first!")
            else:
                sorting()

        case 6:
            if len(li) == 0:
                print("Please enter data first!")
            else:
                min_val, max_val, total, avg = dataset_statistics(li)

                print("\nDataset Statistics:")
                print("- Minimum value:", min_val)
                print("- Maximum value:", max_val)
                print("- Sum of all values:", total)
                print("- Average value:", round(avg, 2))

        case 7:
            show_info(
                Project="Functional Treat",
                Language="Python",
                Topic="Functions"
            )

        case 8:
            print("Thank You for Using the Program!")
            break

        case _:
            print("Invalid Choice! Please try again.")