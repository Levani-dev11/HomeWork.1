
orders = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]

unique_orders = []
for item in orders:
    if item not in unique_orders:
        unique_orders.append(item)

frequency_list = [(item, orders.count(item)) for item in unique_orders]

most_popular_product = ""
max_count = 0

for product, count in frequency_list:
    if count > max_count:
        max_count = count
        most_popular_product = product

last_three_reversed = orders[:-4:-1]

print(f"უნიკალური: {unique_orders}")
print(f"სიხშირე: {frequency_list}")
print(f"ყველაზე პოპულარული: {most_popular_product} ({max_count}-ჯერ)")
print(f"ბოლო 3 შეკვეთა: {last_three_reversed}")
