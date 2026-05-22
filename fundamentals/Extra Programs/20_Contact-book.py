contacts = {}

def add_contact():
    name = input("Enter name: ").lower()
    number = input("Enter phone number: ")

    contacts[name] = number
    print("Contact added successfully.")


def search_contact():
    name = input("Enter name to search: ").lower()

    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").lower()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def show_contacts():
    if len(contacts) == 0:
        print("No contacts available.")

    else:
        print("\n===== CONTACT LIST =====")

        for name, number in contacts.items():
            print(f"{name} : {number}")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        show_contacts()

    elif choice == "5":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice. Try again.")