guests = ["Adam", "Amber", "Alex"]

print(f"{guests[1]} cannot make it.")

guests[1] = "Alice"

print(f"{guests[0]}, you are invited.")
print(f"{guests[1]}, you are invited.")
print(f"{guests[2]}, you are invited.")


# found a new table

print("I found a bigger dinner table.")

guests.insert(0, "Alisha")
guests.insert(2, "Anna" )
guests.append("Amy")

print(f"{guests[0]}, you are invited.")
print(f"{guests[1]}, you are invited.")
print(f"{guests[2]}, you are invited.")
print(f"{guests[3]}, you are invited.")
print(f"{guests[4]}, you are invited.")
print(f"{guests[5]}, you are invited.")