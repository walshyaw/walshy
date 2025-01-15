# ALEX WALSH
# Created on 01/14/2025. Last modified on 01/14/2025.
# https://github.com/walshyaw/

import os
import json
from colorama import Fore

# COLOR FORMATTING.
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

def main():

    # INITALIZE CONTACT DICTIONARY AND CONTACT OPTIONS.
    contacts = init_contacts()
    choices = ["1", "2", "3", "4", "5"]

    print()

    # INITALIZE THE CONTACT CLI PROGRAM
    while True:

        print(f"{GREEN}\033[1mCONTACT LIST\033[0m\n{RESET}")
        print("1. List Contacts")
        print("2. Add a Contact")
        print("3. Delete a Contact")
        print("4. Modify a Contact")
        print("5. Save and Exit\n")

        temp = input("\033[1mEnter your choice:\033[0m ")
        while temp not in choices:
            temp = input("\033[1mEnter your choice (1-5):\033[0m ")
        
        match temp:

            case "1":
                print_contacts(contacts)
            
            case "2":
                contacts = add_contact(contacts)
            
            case "3":
                contacts = delete_contact(contacts)
            
            case "4":
                contacts = modify_contact(contacts)
            
            case "5":
                save_contacts(contacts)
                print(f"\n{GREEN}\033[1m--------------------------\033[0m{RESET}")
                print(f"{GREEN}\033[1m\n   Saving and exiting...\033[0m{RESET}")
                print(f"\n{GREEN}\033[1m--------------------------\033[0m{RESET}\n")
                break

def print_contacts(contacts):

    # PRINTS THE CURRENT CONTACT LIST
    print(f"\n{GREEN}\033[1m--------------------------\033[0m{RESET}")
    for name, phone in contacts.items():
        print(name, end= " - ")
        print(phone)
    print(f"{GREEN}\033[1m--------------------------\033[0m{RESET}\n")
    os.system("pause")
    print()

def add_contact(contacts):

    # REQUESTS USER TO INPUT A NAME AND PHONE NUMBER FOR THEIR NEW CONTACT.
    name = input("\nEnter a name for your new contact: ")
    phone = input("Enter a phone number for your new contact (XXX-XXX-XXXX): ")

    # INPUT VALIDATION TO CONFIRM THAT THE PHONE NUMBER IS VALID.
    while len(phone) != 12:
        print(f"{RED}\n\033[1mInvalid Response.\033[0m{RESET} Phone number is invalid, please follow the format provided.")
        phone = input("Enter a phone number for your new contact (XXX-XXX-XXXX): ")
    
    print()
    # UPDATES AND RETURNS THE DICTIONARY.
    contacts.update({name : phone})
    return contacts

def delete_contact(contacts):

    print_contacts(contacts)
    
    # REQUESTS USER TO INPUT A CONTACT THAT THEY WOULD LIKE DELETED.
    temp = input(f"Who would you like to {RED}delete?{RESET}: ")

    while temp not in contacts.keys():
        temp = input(f"{RED}\n\033[1mInvalid Response.\033[0m{RESET} Contact not found in list. Please try again: ")
    
    print()
    # DELETES THE CONTACT AND RETURNS THE DICTIONARY.
    contacts.pop(temp)
    return contacts

def modify_contact(contacts):
    
    print_contacts(contacts)

    # REQUESTS USER TO INPUT THE NAME OF THE CONTACT THEY WOULD LIKE TO MODIFY.
    name = input("Enter the name of the contact you would like to modify: ")

    while name not in contacts.keys():
        name = input(f"{RED}\n\033[1mInvalid Response.\033[0m{RESET} Contact must be a valid contact.: ")

    # REQUESTS USER TO INPUT WHETHER OR NOT THEY WOULD LIKE TO MODIFY THE NAME OR PHONE NUMBER.
    temp = input("\nWould you like to modify their name or phone number? (N, P): ")

    while temp != "N" and temp != "P":
        temp = input(f"{RED}\n\033[1mInvalid Response.\033[0m{RESET} Please enter N for name or P for phone number: ")

    # CHANGES NAME.
    if temp == "N":
        temp = input("\nEnter a new name for your contact: ")
        contacts[temp] = contacts.pop(name)

    # CHANGES PHONE NUMBER.
    elif temp == "P":
        temp = input("\nEnter a new phone number for your contact: ")

        while len(temp) != 12:
            print(f"{RED}\n\033[1mInvalid Response.\033[0m{RESET} Phone number is invalid, please follow the format provided.")
            temp = input("Enter a phone number for your new contact (XXX-XXX-XXXX): ")
        
        contacts[name] = temp
    
    print()
    # RETURNS THE CONTACTS DICTIONARY.
    return contacts

def init_contacts():

    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, "contacts.json")

    # CHECKS IF PROGRAM HAS BEEN RAN BEFORE. IF NOT, CREATES A NEW CONTACT LIST
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump({}, file)
    
    # INITALIZES THE CONTACT LIST AND RETURNS IT.
    with open(file_path, "r") as file:
        contacts = json.load(file)
    
    return contacts

def save_contacts(contacts):

    # WRITES TO CONTENTS OF THE MODIFIED CONTACTS DICTIONARY TO THE 'contacts.json' FILE.
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, "contacts.json")

    with open(file_path, "w") as file:
        json.dump(contacts, file, indent=4)

if __name__ == "__main__":
    main()