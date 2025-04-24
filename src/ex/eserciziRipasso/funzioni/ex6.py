def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    contactInfo: dict = {'profile' : name, 'email' : email, 'telefono': telefono}
    return contactInfo

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    if name:
        dictionary['profile'] = name
    if email:    
        dictionary['email'] = email
    if telefono:
        dictionary['telefono'] = telefono
    return dictionary


contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))
