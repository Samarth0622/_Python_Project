contacts ={}

while True:
    print("\n Contact Book APP")
    print("1. Add Contact")
    print("2. View  Contact")
    print("3. Update Contact")
    print("4. Delete Contact ")
    print("5. Search Contact") 
    print("6. count Contact")
    print("7. Exit ")

    choice = input("Enter your Choice:")

    if choice == "1":
        name = input("enter your name = ")
        if name in contacts:
            print("Contact already exists.")
        else:
            age = input("enter your age = ")
            email = input("enter your email = ")
            mobile = input("enter your mobile = ")
            contacts[name] = {
                age: int(age),
                email: email,
                mobile: mobile
            }
            print(f'contact name {name} added successfully!') 

    elif choice == '2':
        name = input("enter your name to view = ")
        if name in contacts:
            contact = contacts[name]
            print(f'name:{name}, age:{age}, email:{email}, mobile:{mobile}')
        else:
            print("contact not found.")
    
    elif choice == '3':
        name = input("enter your name to update = ")
        if name in contacts:
            age = input("enter Updated your age = ")
            email = input("enter Updated your email = ")
            mobile = input("enter Updated your mobile = ")
            contacts[name]= {age: int(age),
                email: email,
                mobile: mobile}
        else:
            print("contact not found.")

    elif choice == '4':
        name = input("enter your name to Delete = ")
        if name in contacts:
            del contact[name]
            print(f'contact {name} deleted successfully!')
        else:
            print("contact not found.")

    elif choice == '5':
        search_name = input("enter your name to Search = ")
        found =  False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Contact found: {name}, Age: {age} Email: {email}, Mobile: {mobile}')
                found = True
            if not found:
                print("Contact not found.")

    elif choice == '6':
        print(f"Total contacts: {len(contacts)}")

    elif choice == '7':
        print("Exiting the Contact Book APP.")
        break

    else:
        print("invalid choice. Please try again.")