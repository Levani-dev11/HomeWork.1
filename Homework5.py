print("=== მაღაზიის ფასდაკლების სისტემა ===")

total_amount_text = input("ყიდვის თანხა (ლარი): ")
promo_code = input("პრომო-კოდი (თუ არ გაქვთ — Enter): ").strip()

total_amount = float(total_amount_text)

if total_amount >= 200:
    discount_percent = 20
elif total_amount >= 100:
    discount_percent = 10
elif total_amount >= 50:
    discount_percent = 5
else:
    discount_percent = 0


final_price = total_amount * (1 - discount_percent / 100)

if promo_code.lower() == "vip":
    print("🎁 VIP კოდი: დამატებით -5 ლარი")
    final_price -= 5

print(f"ფასდაკლება: {discount_percent}%")
print(f"გადასახდელი: {final_price:.2f} ლარი")
