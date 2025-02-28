current_users : list = ["Popa","Lucs","Lols","Pierlion","Damien"]

new_users : list = ["LeBonBon","Alex","Popa","Lucs","Shrek"]

current_usersl = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_usersl:
        print(f"{user} is taken. Enter a new name")
    else:
        print("Username is available")