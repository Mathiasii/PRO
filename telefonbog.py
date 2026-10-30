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
    """ tjekker om navnet er der og giver nummeret """
    search = input("Intast navn: ")
    if search in contacts:
        print(contacts[search])
    else:
        print("Not in contacts")

def add_contact():
    """ tilføjer et navn og nummer til dictionary """
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts[name] = number
    print(f"Contact {name} added with number {number}")
    

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








    

    
