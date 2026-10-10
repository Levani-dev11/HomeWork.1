prices = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}
stock = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}

orders = [
    ("ნინო", "ლეპტოპი", 1),
    ("გიორგი", "მაუსი", 3),
    ("ანა", "კლავიატურა", 1),
    ("ნინო", "მაუსი", 2),
    ("გიორგი", "კლავიატურა", 1),
    ("ანა", "ტელეფონი", 1),
    ("ლუკა", "ლეპტოპი", 1),
    ("ლუკა", "მონიტორი", 5),
]

spent = {}
failed_customers = set()

for customer, product, quantity in orders:
    if product not in prices:
        print(f"❌ {customer}: '{product}' არ იყიდება")
        failed_customers.add(customer)

    elif stock[product] < quantity:
        print(f"⚠️ {customer}: {product} — მარაგში მხოლოდ {stock[product]} ცალია")
        failed_customers.add(customer)

    else:
        stock[product] -= quantity
        total = prices[product] * quantity
        spent[customer] = spent.get(customer, 0) + total
        print(f"✅ {customer}: {product} x{quantity} = {total} ლარი")

print("--- ანგარიში ---")

for customer, amount in spent.items():
    print(f"{customer}: {amount} ლარი")

print(f"შემოსავალი: {sum(spent.values())} ლარი")

sold_out = []
for product, quantity in stock.items():
    if quantity == 0:
        sold_out.append(product)

print(f"ამოიწურა: {sorted(sold_out)}")
print(f"წარუმატებელი შეკვეთა ჰქონდათ: {sorted(failed_customers)}")
