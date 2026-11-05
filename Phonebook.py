
# Dictionary to store contact names and phone numbers
contacts = {}


# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added successfully!")


# Function to search for a contact
def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("Phone Number:", contacts[name])
    else:
        print("Contact not found!")


# Function to delete a contact
def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


# Function to display all contacts
def list_contacts():
    if len(contacts) == 0:
        print("Phonebook is empty!")
    else:
        print("\n--- All Contacts ---")
        for name, phone in contacts.items():
            print("Name:", name, "| Phone:", phone)


# Function to display the menu and run the phonebook
def main():
    while True:
        print("\n===== PHONEBOOK MENU =====")
        print("1. Add a Contact")
        print("2. Search for a Contact")
        print("3. Delete a Contact")
        print("4. List All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Start the phonebook application
main()
