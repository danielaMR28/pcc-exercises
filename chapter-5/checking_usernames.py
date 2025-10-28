current_users = ["Maria", "Juan", "Manuel", "DANIELA", "Ana"]

new_users = ["Pedro", "Lulu", "JUAN", "Pepe", "Daniela"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for nuser in new_users:
    if nuser.lower() in current_users_lower:
        print("You need to enter a new username")
    else:
        print("The username is available")