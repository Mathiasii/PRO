contacts = {
    "Mikkel" : "3975718",
    "Elias" : "4561827",
    "Max" : "2518953"
}

def goodbye():
    """ prints the text beneath """
    print("Thanks for havng used the telefonbog")

def all_contacts():
    """ prints all contacts """
    print(contacts)

def find_contact():
    """ checks name and number if it's in it gives that name and number """
    search = input("Intast navn: ")
    if search in contacts:
        print(contacts[search])
    else:
        print("Not in contacts")

def add_contact():
    """ tilføjer et navn og nummer til dictionary """
    name = input("Indtast navn: ")
    number = input("Indtast nummer: ")
    contacts[name] = number
    print(f"Kontakt {name} tilføjet med nummeret {number}")
    

while True:
    print("\n1 Add contact")
    print("2 Find contact")
    print("3 Show all contacts")
    print("4 Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    
    if choice == "2":
        find_contact()

    if choice == "3":
        all_contacts()
        input()

    if choice == "4":
        goodbye()
        break
