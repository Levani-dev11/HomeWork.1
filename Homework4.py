age = int(input("ასაკი: "))
parent = input("მშობელთან ერთად ხართ? (კი/არა): ").strip().lower()

if (age >= 18) or (age >= 12 and age <= 17 and parent == "კი"):
    print("შესვლა დაშვებულია")
else:
    print("შესვლა აკრძალულია")