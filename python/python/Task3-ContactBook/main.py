# CODSOFT – Python Task 3: Contact Book

contacts = []

def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")

def search_contact():
    search_name = input("\nEnter name to search: ").lower()
    for contact in contacts:
        if contact["name"].lower() == search_name:
            print("\n✅ Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            return
    print("❌ Contact not found.")

def update_contact():
    search_name = input("\nEnter name to update: ").lower()
    for contact in contacts:
        if contact["name"].lower() == search_name:
            print("\n--- Enter new details (leave blank to keep old value) ---")
            name = input(f"New name ({contact['name']}): ") or contact['name']
            phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
            email = input(f"New email ({contact['email']}): ") or contact['email']
            address = input(f"New address ({contact['address']}): ") or contact['address']

            contact.update({"name": name, "phone": phone, "email": email, "address": address})
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

def delete_contact():
    search_name = input("\nEnter name to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == search_name:
            contacts.remove(contact)
            print("✅ Contact deleted successfully!")
            return
    print("❌ Contact not found.")


def main():
    while True:
        print("\n===== CONTACT BOOK (CODSOFT TASK 3) =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you! Task 3 completed.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
