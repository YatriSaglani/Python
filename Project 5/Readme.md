# 🏢 Employee Management System (OOP Wrapper)

A simple **menu-driven Employee Management System** developed in **Python** using **Object-Oriented Programming (OOP)** concepts. This project demonstrates **Encapsulation**, **Inheritance**, **Method Overriding**, and the use of **Constructors** to manage different types of employees.

---

## 📌 Features

- ➕ Create Employee records
- 👨‍💼 Create Manager records
- 👨‍💻 Create Developer records
- 📋 Display Employee, Manager, and Developer details separately
- 🔒 Uses private attributes for data security (Encapsulation)
- 🧬 Demonstrates Inheritance and Method Overriding
- 📑 Interactive menu-driven interface

---

## 🛠️ OOP Concepts Used

### 1. Encapsulation
- Employee data members are declared as private using double underscores (`__`).
- Data can only be accessed through class methods.

### 2. Inheritance
- `Manager` and `Developer` classes inherit from the `Employee` class.

### 3. Method Overriding
- Both child classes override the `ShowInfo()` method to display additional information.

### 4. Constructors
- Constructors (`__init__`) are used to initialize object data.

---

## 📂 Class Structure

```
Employee
│
├── Manager
│
└── Developer
```

### Employee
- Employee ID
- Name
- Age
- Salary

### Manager
- Inherits Employee
- Department

### Developer
- Inherits Employee
- Programming Language

---

## 📜 Menu Options

```
========== EMPLOYEE MANAGEMENT SYSTEM ==========
1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit
```

The **Show Details** menu allows you to display:

- Employees
- Managers
- Developers


---

## 💻 Sample Output

```
========== EMPLOYEE MANAGEMENT SYSTEM ==========
1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit

Enter your choice : 1

Enter Employee ID : 101
Enter Employee Name : John
Enter Employee Age : 25
Enter Employee Salary : 35000

Employee created successfully.
```

---

## 📚 Technologies Used

- Python 3
- Object-Oriented Programming

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Classes and Objects
- Constructors
- Encapsulation
- Inheritance
- Method Overriding
- `super()` function
- Lists of Objects
- Menu-driven programming
- Python `match-case` statement

---

## 🚀 Future Improvements

- Update employee records
- Delete employee records
- Search employees by ID
- File handling for permanent data storage
- Exception handling for invalid inputs
- GUI version using Tkinter or PyQt

---

## 👨‍💻 Author

**Yatri Saglani**

Computer Engineering Student | Python Learner  

