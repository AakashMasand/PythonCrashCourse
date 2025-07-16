guests = ["Adam", "Amber", "Alex"]

print(f"{guests[1]} cannot make it.")

guests[1] = "Alice"

print(f"{guests[0]}, you are invited.")
print(f"{guests[1]}, you are invited.")
print(f"{guests[2]}, you are invited.")



#------------

print("I can invite only two guests.")

print(f"{guests.pop()}, I am sorry, I cannot invite you to dinner")

print(f"{guests[0]}, you are still invited.")
print(f"{guests[1]}, you are still invited.")

del guests[1]
del guests[0]

print(guests)