# Personal Journal Manager

## 📌 Project Description

**Personal Journal Manager** is a simple Python-based project that allows users to create, view, search, and delete journal entries.

The project uses **file handling** to store journal entries in a text file. Each entry contains the date, day, time, topic, and journal text.

---

## 🛠️ Technologies Used

* Python
* File Handling
* `datetime` module
* `os` module

---

## ✨ Features

1. Add a new journal entry
2. View all journal entries
3. Search journal entries by keyword or date
4. Delete all journal entries
5. Exit the program

---

# 📚 Exercises / Features

## 1. Add New Journal Entry

This option allows the user to add a new journal entry.

The user enters:

* Topic
* Journal entry

The program automatically records the **date, day, and time** when the entry is added. The information is then saved in the journal text file.

### 📸 Output Screenshot

> **Screenshot 1: Add New Journal Entry**
<br>
    !["Screenshot 1"](Output%201.jpg)

<br><br><br>

---

## 2. View All Entries

This option displays all the journal entries stored in the journal file.

If there are no entries, the program displays a message informing the user that no journal entries are available.

### 📸 Output Screenshot

> **Screenshot 2: View All Journal Entries**
<br>
    !["Screenshot 2"](Output%202.jpg)
<br><br><br>

---

## 3. Search Journal Entries

This option allows the user to search for journal entries using a **keyword or date**.

The program checks the stored entries and displays the matching entries. If no matching entry is found, it displays an appropriate message.

### 📸 Output Screenshot

> **Screenshot 3: Search Journal Entries**
<br>
    !["Screenshot 3"](Output%203.jpg)

<br><br><br>

---

## 4. Delete All Entries

This option allows the user to delete all the journal entries.

Before deleting the entries, the program asks the user for confirmation. If the user enters `yes`, all stored entries are removed. Otherwise, the deletion is cancelled.

### 📸 Output Screenshot

> **Screenshot 4: Delete Journal Entries**
   <br>
    !["Screenshot 4"](Output%204.jpg)

<br><br><br>
---

# 📋 Main Menu

When the program starts, it displays the following menu:

```text
Welcome to Personal Journal Manager!

Select an option:

1. Add new entry
2. View all entries
3. Search by topic
4. Delete all entries
5. Exit
```

The user can select an option by entering a number from **1 to 5**.

---

## 📁 Project Structure

```text
Project 6/
│
├── File_Operator.py
└── Journal.txt
```

* **File_Operator.py** → Contains the Python program.
* **Journal.txt** → Stores the journal entries.

---

## 🎯 Learning Outcomes

Through this project, the following concepts are practiced:

* Python functions
* User input
* File handling
* Reading and writing text files
* Searching text in files
* Using `datetime`
* Using the `os` module
* Conditional statements
* Loops
* Menu-driven programs

---

## 👩‍💻 Conclusion

The **Personal Journal Manager** is a simple Python project designed to demonstrate the practical use of file handling. It provides basic functionality for managing journal entries through a menu-driven interface.
