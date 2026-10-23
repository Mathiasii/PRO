contacts = {
    "Mikkel" : "3975718",
    "Elias" : "4561827",
    "Max" : "2518953"
}

def goodbye():
    print("Thanks for havng used the telefonbog")

def all_contacts():
    print(*contacts)

def find_contact():
    search = input("Intast navn: ")
    if search in contacts:
        print(contacts[search])
    else:
        print("Not in contacts")
    

while True:
    print("\n1 Add contact")
    print("2 Find contact")
    print("3 Show all contacts")
    print("4 Exit")
    choice = input("Choose an option: ")

    if choice == "2":
        find_contact()

    if choice == "3":
        all_contacts()
        input()

    if choice == "4":
        goodbye()
        break








    

    
