class Employee:
    def __init__(self, empId, name, age, salary):
        self.__empId = empId
        self.__name = name
        self.__age = age
        self.__salary = salary

    def ShowInfo(self):
        print(f"Employee ID : {self.__empId}")
        print(f"Name        : {self.__name}")
        print(f"Age         : {self.__age}")
        print(f"Salary      : {self.__salary}")


class Manager(Employee):
    def __init__(self, empId, name, age, salary, department):
        super().__init__(empId, name, age, salary)
        self.__department = department

    def ShowInfo(self):
        super().ShowInfo()
        print(f"Department  : {self.__department}")

class Developer(Employee):
    def __init__(self, empId, name, age, salary, programming):
        super().__init__(empId, name, age, salary)
        self.__programming = programming

    def ShowInfo(self):
        super().ShowInfo()
        print(f"Programming Language : {self.__programming}")


employees = []
managers = []
developers = []

while True:

    print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("\nEnter your choice : "))

    match choice:

        case 1:
            empId = int(input("Enter Employee ID : "))
            name = input("Enter Employee Name : ")
            age = int(input("Enter Employee Age : "))
            salary = float(input("Enter Employee Salary : "))

            Eobj = Employee(empId, name, age, salary)
            employees.append(Eobj)

            print("\nEmployee created successfully.\n")

        case 2:
            empId = int(input("Enter Manager ID : "))
            name = input("Enter Manager Name : ")
            age = int(input("Enter Manager Age : "))
            salary = float(input("Enter Manager Salary : "))
            department = input("Enter Department : ")

            Mobj = Manager(empId, name, age, salary, department)
            managers.append(Mobj)

            print("\nManager created successfully.\n")

        case 3:
            empId = int(input("Enter Developer ID : "))
            name = input("Enter Developer Name : ")
            age = int(input("Enter Developer Age : "))
            salary = float(input("Enter Developer Salary : "))
            programming = input("Enter Programming Language : ")

            Dobj = Developer(empId, name, age, salary, programming)
            developers.append(Dobj)

            print("\nDeveloper created successfully.\n")

        case 4:
            print("\n1. Show Employees")
            print("2. Show Managers")
            print("3. Show Developers")

            subCh = int(input("\nEnter your choice : "))

            if subCh == 1:
                if len(employees) == 0:
                    print("\nNo Employee Records Found.\n")
                else:
                    print("\n------ Employee Details ------")
                    for emp in employees:
                        emp.ShowInfo()
                        print("-" * 35)

            elif subCh == 2:
                if len(managers) == 0:
                    print("\nNo Manager Records Found.\n")
                else:
                    print("\n------ Manager Details ------")
                    for mgr in managers:
                        mgr.ShowInfo()
                        print("-" * 35)

            elif subCh == 3:
                if len(developers) == 0:
                    print("\nNo Developer Records Found.\n")
                else:
                    print("\n------ Developer Details ------")
                    for dev in developers:
                        dev.ShowInfo()
                        print("-" * 35)

            else:
                print("\nInvalid Choice!\n")
                
        case _:
            print("\nInvalid Choice! Please try again.\n")