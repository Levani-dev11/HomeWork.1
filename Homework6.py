sityva = input("შეიყვანე სიტყვა: ")
samძებნი_simbolo = input("რომელი სიმბოლო დავთვალოთ: ")

raodenoba = 0

for simbolo in sityva:
    if simbolo == samძებნი_simbolo:
        raodenoba += 1

print(f"სიმბოლო {samძებნი_simbolo} გვხვდება {raodenoba} -ჯერ")
