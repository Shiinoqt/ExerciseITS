class ContactManager:
    contacts: dict

    def __init__(self, contacts: dict[str,list[str]]):
        self.contacts = contacts

    def create_contact(self, name: str, phone_numbers: list[str]):
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
        else:
            raise ValueError("Errore: il contatto esiste già")
        # Return a new dictionary with only the new contact
        return {name: phone_numbers}

    def add_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: Il contatto non esiste")
        if phone_number in self.contacts[contact_name]:
            raise ValueError("Errore: Il numero di telefono esiste già")
        else:
            self.contacts[contact_name].append(phone_number)
        # Return a new dictionary with the updated contact
        return {contact_name: list(self.contacts[contact_name])}

    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: Il contatto non esiste.")
        if phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: Il numero di telefono non è presente")
        else:
            self.contacts[contact_name].remove(phone_number)
        # Return a new dictionary with the updated contact
        return {contact_name: list(self.contacts[contact_name])}

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: Il contatto non esiste.")
        if old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: Il numero di telefono non è presente")
        else:
            index: int = self.contacts[contact_name].index(old_phone_number)
            self.contacts[contact_name][index] = new_phone_number
    
            #self.contacts[contact_name].remove(old_phone_number)
            #self.contacts[contact_name].append(new_phone_number)
        # Return a new dictionary with the updated contact
        return {contact_name: list(self.contacts[contact_name])}

    def list_contacts(self):
        return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name: str):
        if contact_name not in self.contacts:
            raise ValueError("Errore: Il contatto non esiste.") 
        return self.contacts[contact_name]
    
    def search_contact(self, phone_number: str):
        result: list[str] = []
        for contact, numbers in self.contacts.items():
            if phone_number in numbers:
                result.append(contact)
        if not result:
            raise Exception("Nessun contatto trovato")
        
        return result

if __name__ == "__main__":
    contatti = {}
    numbers = ["3231321", "321313123", "32111123"]
    lista1 = ContactManager(contatti)
    print("Create contact:")
    print(lista1.create_contact("Giorgio", numbers))
    print("Add phone number:")
    print(lista1.add_phone_number("Giorgio", "332112311"))
    print("Remove phone number:")
    print(lista1.remove_phone_number("Giorgio", "321313123"))
    print("Update phone number:")
    print(lista1.update_phone_number("Giorgio", "3231321", "333333333"))
    print("List contacts:")
    print(lista1.list_contacts())
    print("List phone numbers for Giorgio:")
    print(lista1.list_phone_numbers("Giorgio"))
    print(lista1.search_contact("333333333"))

