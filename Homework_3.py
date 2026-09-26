bill = float(input("ჩეკის თანხა: "))
tip_percent = int(input("ჩაის ფული (%): "))
people = int(input("ადამიანების რაოდენობა: "))

tip_amount = bill * tip_percent / 100
full_bill = bill + tip_amount
one_person_bill = full_bill / people

print("ჩაის ფული:", round(tip_amount, 2))
print("სულ გადასახდელი:", round(full_bill, 2))
print("თითო ადამიანზე:", round(one_person_bill, 2))