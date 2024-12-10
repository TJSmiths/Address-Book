from colorama import Fore, Style

# This class is to show an individual contact with a name, phone number and email
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

# This class is to show the contact book that contains a list of contacts
class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact("Alice", "1234567890", "alice@email.com"),
            Contact("Bob", "9876543210", "bob@email.com")
        ]

    # Funtion to add contact
    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name, phone_number, email) # Assign the new contact to a variable
        for contact in self.contacts:
            if new_contact.name == contact.name:
                print(Fore.RED + f"Contact already exists!")
                return
        self.contacts.append(new_contact) # Append the list of contacts with the new variable
        print(Fore.GREEN + f"Contact '{name}' added successfully.") # Confirmation message
        

    # Function to display all contacts
    def display_all_contacts(self):
        if self.contacts: # Check the contacts list is not empty
            print("All Contacts:")
            for contact in self.contacts: # Loop through each contact and print all details
                print(Fore.WHITE + f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
        else:
            print(Fore.RED + f"No contacts found.") # Error message if contacts list is empty
    
    # Function to search for contacts - I have used .lower() to help with case-sensitivity issues
    def search_contact(self):
        searchcontact = input("Please enter the name you would like to search for:").lower() # Assign the search to a variable based on user input
        for contact in self.contacts: # Loop through the list of contacts
            if searchcontact == contact.name.lower(): # If user input is in the list, print the contact details
                print(Fore.GREEN + f"Contact found:")
                print(Fore.WHITE + f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
                return
        print(Fore.RED + f"Contact {searchcontact} not found!") # Error message if user input is not found in contacts list
    
    # Function to update contacts, again using .lower() to help with case sensitivity
    def update_contact(self):
        print("Contacts - ")
        for contact in self.contacts: # Loop through contacts and print each contacts name to show the user the options
            print(contact.name)
        updatecontact = input("Please enter the name of the contact you would like to update:").lower() # Assign user input to a variable to search for
        for contact in self.contacts: # Loop through the contact list
            if updatecontact == contact.name.lower(): # Check if the contact exists to be updated
                print("1. Name\n2. Phone Number\n3. Email Address") # Print a menu of options asking which field to update
                updatefield = input("Which field would you like to update?\n")
                if updatefield == "1": # Option 1 creates a variable for the new name and updates the contact name to the variable set based on user input
                    newname = input("Please enter the new name for the contact:\n")
                    contact.name = newname
                    print(Fore.GREEN + f"{updatecontact} update successfully!") # Confirmation message
                elif updatefield == "2": # Option 2 creates a variable for the new phone number and updates the contact phone number to the variable set based on user input
                    newnumber = input("Please enter the new phone number for the contact:\n")
                    contact.phone_number = newnumber
                    print(Fore.GREEN + f"{updatecontact} update successfully!") # Confirmation message
                elif updatefield == "3": # Option 3 creates a variable for the new email addres and updates the email address to the variable set based on user input
                    newemail = input("Please enter the new email address for the contact:\n")
                    contact.email = newemail
                    print(Fore.GREEN + f"{updatecontact} update successfully!") # Confirmation message
                else:
                    print("Invalid option. Please select 1, 2, or 3.") # Catch for improper menu selection
                return
        print(Fore.RED + f"Contact not found!") # Error message if contact is not found
    
    # Function to delete contact
    def delete_contact(self):
        print("Contacts - ")
        for contact in self.contacts: # Loop through contacts and print each contacts name to show the user the options
            print(contact.name)
        deletecontact = input("Please choose a contact to delete:\n") # Assign a variable to user input on which contact to delete
        for contact in self.contacts:
            if contact.name == deletecontact: # Check if the contact exists, then remove them from the list
                self.contacts.remove(contact)
                print(Fore.GREEN + f"{deletecontact} deleted successfully.") # Confirmation message
                break
        else:
            print(Fore.RED + f"The contact '{deletecontact}' does not exist.")
    
    #Function to sort existing contacts
    def sort_contacts(self):
        self.contacts = sorted(self.contacts, key=lambda contact: contact.name) # The info on how to do this was obtained from https://stackoverflow.com/questions/48727337/python-how-to-sort-list-of-object
        print(Fore.GREEN + f"Contact list sorted alphabetically!")

# Main function to handle the running of the program
def main():
    contact_book = ContactBook()

    while True: # While loop to provide options menu for the user
        print(Fore.GREEN + f"\n--- Contact Book Menu ---")
        print(Fore.BLUE + f"1. Add New Contact")
        print(Fore.BLUE + f"2. Show All Contacts")
        print(Fore.BLUE + f"3. Search Contact")
        print(Fore.BLUE + f"4. Update Contact")
        print(Fore.BLUE + f"5. Delete Contact")
        print(Fore.BLUE + f"6. Sort Contacts")
        print(Fore.RED + f"0. Exit")

        choice = input(Fore.WHITE + f"Enter your choice: ") # Input for user to choose an option, this is assigned to a variable

        # For the menu, I have linked the menu options to their corresponding functions.
        # This could alse be done for option 1 by creating an "adduser" function, but no point changing the code provided since it works
        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == "2":
            contact_book.display_all_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            contact_book.sort_contacts()
        elif choice == "0":
            print("Exiting Contact Book. Goodbye!")
            break # This break will exit the program
        else:
            print("Please choose an option from the menu!") # Error for incorrect choices

if __name__ == "__main__": # Launch the main function to run the program
    main()

