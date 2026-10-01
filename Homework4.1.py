a = int(input("პირველი რიცხვი: "))
b = int(input("მეორე რიცხვი: "))
c = int(input("მესამე რიცხვი: "))

if a >= b and a >= c:
    print("უდიდესი რიცხვია:", a)
elif b >= a and b >= c:
    print("უდიდესი რიცხვია:", b)
else:
    print("უდიდესი რიცხვია:", c)