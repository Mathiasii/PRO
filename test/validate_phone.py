# Tre udgaver af validate_phone_number
# Alle udgaver: fjerner whitespace, tjekker længde og at der kun er cifre


# Udgave 1: simpel - returnerer True/False
def validate_phone_number(phone):
    phone = "".join(phone.split())  # fjern al whitespace (mellemrum, tabs osv.)
    return len(phone) == 8 and phone.isdigit()


# Udgave 2: kan konfigureres med parametre
def validate_phone_number_config(phone, length=8, remove_whitespace=True):
    if remove_whitespace:
        phone = "".join(phone.split())
    return len(phone) == length and phone.isdigit()


# Udgave 3: returnerer (succes, fejlbesked, formateret nummer)
def validate_phone_number_full(phone, length=8, remove_whitespace=True):
    if remove_whitespace:
        phone = "".join(phone.split())

    if phone == "":
        return False, "Telefonnummeret er tomt", None
    if not phone.isdigit():
        return False, "Telefonnummeret må kun indeholde cifre", None
    if len(phone) != length:
        return False, f"Telefonnummeret skal være {length} cifre (fik {len(phone)})", None

    return True, "", phone


if __name__ == "__main__":
    tests = ["12345678", "12 34 56 78", " 1234 5678 ", "1234567", "1234abcd", ""]

    print("Udgave 1:")
    for t in tests:
        print(f"  {t!r:16} -> {validate_phone_number(t)}")

    print("\nUdgave 2 (length=6):")
    for t in ["123456", "12 34 56", "12345678"]:
        print(f"  {t!r:16} -> {validate_phone_number_config(t, length=6)}")

    print("\nUdgave 3:")
    for t in tests:
        ok, msg, number = validate_phone_number_full(t)
        print(f"  {t!r:16} -> {ok}, {msg!r}, {number!r}")
