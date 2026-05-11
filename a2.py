contacts = [{"name": "ram", "phone": "9899999999", "email": "ram123@email.com"},{"name": "sita", "phone": "1122334455", "email": "sita@email.com"}]
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10
def validate_email(email):
    return "@" in email and len(email) > 3
while True:
    print("\n--- Contact Book Application ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number (10 digits): ")
        email = input("Enter email address: ")
        if not validate_phone(phone):
            print("Invalid phone number. Must be 10 digits.")
        elif not validate_email(email):
            print("Invalid email format. Must contain '@'.")
        else:
            contacts.append({"name": name, "phone": phone, "email": email})
            print(f"Contact '{name}' added successfully!")
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nList of Contacts:")
            for index, contact in enumerate(contacts):
                print(f"{index} → Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    elif choice == "3":
        if len(contacts) == 0:
            print("No contacts available to update.")
        else:
            try:
                index = int(input("Enter index number to update: "))
                if 0 <= index < len(contacts):
                    print(f"Current Contact → Name: {contacts[index]['name']}, Phone: {contacts[index]['phone']}, Email: {contacts[index]['email']}")
                    new_name = input("Enter new name (leave blank to keep current): ")
                    new_phone = input("Enter new phone (10 digits, leave blank to keep current): ")
                    new_email = input("Enter new email (leave blank to keep current): ")
                    if new_name.strip():
                        contacts[index]['name'] = new_name
                    if new_phone.strip():
                        if validate_phone(new_phone):
                            contacts[index]['phone'] = new_phone
                        else:
                            print("Invalid phone number. Keeping old value.")
                    if new_email.strip():
                        if validate_email(new_email):
                            contacts[index]['email'] = new_email
                        else:
                            print("Invalid email format. Keeping old value.")
                    print("Contact updated successfully!")
                else:
                    print("Invalid index number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == "4":
        if len(contacts) == 0:
            print("No contacts available to delete.")
        else:
            try:
                index = int(input("Enter index number to delete: "))
                if 0 <= index < len(contacts):
                    removed_contact = contacts.pop(index)
                    print(f"Contact '{removed_contact['name']}' deleted successfully!")
                else:
                    print("Invalid index number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == "5":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            search_name = input("Enter name to search: ").lower()
            found_contacts = [contact for contact in contacts if search_name in contact['name'].lower()]
            if found_contacts:
                print("\nSearch Results:")
                for contact in found_contacts:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("Contact not found.")
    elif choice == "6":
        print("Exiting Contact Book Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")