#!/usr/bin/env python
# coding: utf-8

# In[1]:


contact = {}

print("Choose your action: \n"
      "1.) Add contact \n"
      "2.) View All Contacts \n"
      "3.) Search Contact \n"
      "4.) Update Contact \n"
      "5.) Delete Contact \n"
      "6.) Exit \n")

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        ph_no = int(input("Enter the phone number: "))
        email = input("Enter the email - id: ")
        address = input("Enter the address: ")

        contact[name] = {'phone': ph_no, 'email': email, 'address': address}
        print("Contact Saved")

    elif choice == 2:
        print(contact)

    elif choice == 3:
        search_contact = input("Enter the name: ")
        if search_contact in contact:
            print(search_contact, "The name is found: ", contact[search_contact])
        else:
            print("No results found")

    elif choice == 5:
        del_contact = input("Enter the name of the contact you would like to delete: ")
        if del_contact in contact:
            del contact[del_contact]
            print("Contact deleted.")
        else:
            print("No such contact found")

    elif choice == 4:
        search_contact1 = input("Enter the name: ")
        if search_contact1 in contact:
            print(search_contact1, "The name is found: ", contact[search_contact1])
            print("Enter the changes: ")
            up_ph_no = int(input("Enter the phone number: "))
            up_email = input("Enter the email - id: ")
            up_address = input("Enter the address: ")
            updated_contact = {'phone': up_ph_no, 'email': up_email, 'address': up_address}
            contact[search_contact1] = updated_contact
            print(contact)
        else:
            print("No results found")

    elif choice == 6:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice...!!")

