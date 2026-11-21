guests=["Aizen", "Johan", "Light"]




not_coming=guests.pop(1)
print(f"Guys {not_coming} will not come to dinner")

guests.insert(1, "Naruto")

print(f"I invite you to dinner, {guests[0]}")
print(f"I invite you to dinner, {guests[2]}")
print(f"I invite you to dinner, {guests[1]}")

print("Guys I just found a bigger table!")

guests.insert(0, "Itachi")

guests.insert(2, "Mayuri")


guests.append("Hollow Ichigo")

for x in range (0, 6):
    print(f"I invite you to dinner, {guests[x]}!")


print("Nah man, only 2 people....Yeah I am messing w yall")
print(guests)



print(f"Sorry {guests[0]}, you are cooked")
guests.pop(0)

print(f"Sorry {guests[1]}, you are cooked")
guests.pop(0)


print(f"Sorry {guests[2]}, you are cooked")
guests.pop(0)


print(f"Sorry {guests[0]}, you are cooked")
guests.pop(0)
print(guests)


for bro in guests:
    print(f"You are still invited {bro}")






