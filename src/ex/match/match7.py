perm : dict = {"name":[], "role":[],"age":[]}

name = str(input("Digitare nome utente: "))
perm["name"] = name

role = str(input("Digitare ruolo dell'utente: "))
perm["role"] = role

age = int(input("Digitare l'eta dell'utente: "))
perm["age"] = age

# match perm:
#     case {"role": "admin"}:
#         print("Accesso completo a tutte le funzionalità")
#     case {"role": "mod"}:
#         print(f"Salve {name}! Può gestire i contenuti ma non modificare le impostazioni.")
#     case {"role": "utente"}:
#         if age >= 18:
#             print("Accesso standard a tutti i servizi.")
#         else:
#             print("Accesso limitato!")
#     case {"role": "ospite"}:
#         print("Accesso ristretto! Solo visualizzazione dei contenuti.")
#     case _:
#         print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")

match perm:
    case {"role": "admin"}:
        print("Accesso completo a tutte le funzionalità")
    case {"role": "mod"}:
        print(f"Salve {name}! Può gestire i contenuti ma non modificare le impostazioni.")
    case {"role": "utente"} if age >= 18:
        print("Accesso standard a tutti i servizi.")
    case {"role": "utente"} if age < 18:
        print("Accesso limitato!")
    case {"role": "ospite"}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")