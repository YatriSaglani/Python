import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        print("\n----- Add New Entry -----")
        entry = input("Enter your journal entry:\n")

        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

        try:
            with open(self.filename, "a") as file:
                file.write(f"{timestamp}\n")
                file.write(entry + "\n")
                file.write("-" * 50 + "\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("Permission denied.")
        except Exception as e:
            print("Error:", e)

    def view_entries(self):
        print("\n----- View All Entries -----")

        try:
            with open(self.filename, "r") as file:
                data = file.read()

                if data.strip() == "":
                    print("Journal is empty.")
                else:
                    print(data)

        except FileNotFoundError:
            print("No journal entries found. Start by adding a new entry!")
        except Exception as e:
            print("Error:", e)

    def search_entry(self):
        print("\n----- Search Entry -----")
        keyword = input("Enter keyword or date to search: ")

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            found = False

            for line in lines:
                if keyword.lower() in line.lower():
                    if not found:
                        print("\nMatching Entries:\n")
                    print(line.strip())
                    found = True

            if not found:
                print("No entries found for the keyword:", keyword)

        except FileNotFoundError:
            print("Journal file not found.")
        except Exception as e:
            print("Error:", e)

    def delete_entries(self):
        print("\n----- Delete All Entries -----")

        choice = input("Are you sure? (yes/no): ")

        if choice.lower() == "yes":
            try:
                open(self.filename, "w").close()
                print("All journal entries deleted successfully!")

            except PermissionError:
                print("Permission denied.")

            except Exception as e:
                print("Error:", e)

        else:
            print("Deletion cancelled.")

    def menu(self):

        while True:

            print("\n===================================")
            print("      PERSONAL JOURNAL MANAGER")
            print("===================================")
            print("1. Add New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")
            print("===================================")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.add_entry()

                elif choice == 2:
                    self.view_entries()

                elif choice == 3:
                    self.search_entry()

                elif choice == 4:
                    self.delete_entries()

                elif choice == 5:
                    print("\nThank you for using Personal Journal Manager!")
                    break

                else:
                    print("Invalid choice! Please select between 1-5.")

            except ValueError:
                print("Please enter a valid number.")
            except Exception as e:
                print("Unexpected Error:", e)

if __name__ == "__main__":
    journal = JournalManager()
    journal.menu()