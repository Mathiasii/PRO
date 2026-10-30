contacts = {
    "Mikkel" : "3975718",
    "Elias" : "4561827",
    "Max" : "2518953"
}

def goodbye():
    """ prints the text beneath """
    print("Tak for at have brugt telefonbogen")

def all_contacts():
    """ prints all contacts """
    print(contacts)

def find_contact(name):
    """ checks name if it exists it prints the name and number """
    if name in contacts:
        print(contacts[name])
    else:
        print("Navnet er ikke i telefonbogen")

def add_contact():
    """ tilføjer et navn og nummer til dictionary """
    name = input("Indtast navn: ")
    number = input("Indtast nummer: ")

    ok, message, cleaned = validate_contact(number)
    if not ok:
            print(message)
            return
    
    contacts[name] = number
    print(f"Kontakt {name} tilføjet med nummeret {number}")

def validate_contact(phone, length=8, remove_whitespace=True):
    """ checks if it is a valid phone number """
    if remove_whitespace:
        phone = "".join(phone.split())
     
    if phone == "":
        return False, "Ingen tal i feltet", None
    if not phone.isdigit():
        return False, "Der må kun være tal i telefonnumeret", None
    if len(phone) != length:
        return False, f"Telefonnummeret skal være {length} cifre (fik {len(phone)})", None
    return True, "", phone
   

    

while True:
    print("\n1 Tilføj kontakt")
    print("2 Find kontakt")
    print("3 Vis alle kontakter")
    print("4 Afslut")
    choice = input("Vælg en mulighed: ")

    if choice == "1":
        add_contact()


    if choice == "2":
        search = input("Indtast navn: ")
        find_contact(search)

    if choice == "3":
        all_contacts()
        input()

    if choice == "4":
        goodbye()
        break
