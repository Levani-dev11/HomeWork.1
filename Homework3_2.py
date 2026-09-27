card = "4111222233334444"
phone = "599123456"

masked_card = "**** **** **** " + card[-4:]

first_four = card[:4]
card_length = len(card)
reversed_card = card[::-1]

formatted_phone = f"{phone[:3]} {phone[3:5]} {phone[5:7]} {phone[7:]}"

print(f"შენიღბული: {masked_card}")
print(f"პირველი 4 ციფრი: {first_four}")
print(f"ციფრების რაოდენობა: {card_length}")
print(f"შებრუნებული: {reversed_card}")
print(f"ტელეფონი: {formatted_phone}")