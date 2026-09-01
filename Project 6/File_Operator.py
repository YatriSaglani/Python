import datetime
import os

FILE_PATH = "D:\\Python\\Project 6\\Journal.txt"

def add_entry():
    topic = input("Enter topic: ")
    entry = input("Enter your journal entry: ")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d (%A) %I:%M %p")

    with open(FILE_PATH, "a") as fp:
        fp.write(f"[{timestamp}] Topic: {topic}\nEntry: {entry}\n{'-' * 60}\n")

    print("Entry added successfully!")

def view_entries():
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print("No journal entries found. Start by adding a new entry!")
        return

    with open(FILE_PATH, "r") as fp:
        print(fp.read())

    print("All entries displayed successfully!")

def search_entries():
    keyword = input("Enter a keyword or date to search: ")

    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        print("No journal entries found. Start by adding a new entry!")
        return

    with open(FILE_PATH, "r") as fp:
        entries = fp.read().split("\n----------------------------------------\n")

        found = [entry for entry in entries if keyword.lower() in entry.lower()]

        if found:
            print("Found entries:")

            for entry in found:
                print(entry.strip())
                print("-" * 40)
        else:
            print(f"No entries found for the keyword: {keyword}")

def delete_entries():
    confirmation = input("Are you sure you want to delete all entries? (yes/no): ")

    if confirmation.lower() == "yes":
        open(FILE_PATH, "w").close()
        print("All journal entries have been deleted.")
    else:
        print("Deletion canceled.")

print("\nWelcome to Personal Journal Manager!")

print("Select an option:")

while True:
    print("\n1. Add new entry")
    print("2. View all entries")
    print("3. Search by topic")
    print("4. Delete all entries")
    print("5. Exit\n")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_entry()

    elif choice == "2":
        view_entries()

    elif choice == "3":
        search_entries()

    elif choice == "4":
        delete_entries()

    elif choice == "5":
        print("***Thank you for using Personal Journal Manager. Goodbye!***")
        break

    else:
        print("Invalid option. Please select a valid option from the menu.")

