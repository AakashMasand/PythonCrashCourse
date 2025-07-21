current_users = ["topG", "bottomG", "leftG", "rightG", "middleG"]

new_users = ["Topg", "Bottomg", "Amar", "Akbar", "Anthony"]

lower_current_user = []

for current_user in current_users:
    current_user = current_user.lower()
    lower_current_user.append(current_user)

#print(lower_current_user)

for new_user in new_users:
    new_user = new_user.lower()
    if new_user in lower_current_user:
        print(f"{new_user} will need a new username.")
    else:
        print(f"username {new_user} is available.")