raw_username = "  Super_Coder_2026  "

username = raw_username.strip().lower().replace("_", "-")

length = len(username)
starts_with_super = username.startswith("super")
dash_count = username.count("-")

is_alnum_without_dashes = username.replace("-", "").isalnum()

print(f"მომხმარებლის სახელი: {username}")
print(f"სიგრძე: {length}")
print(f"იწყება 'super'-ით: {starts_with_super}")
print(f"ტირეების რაოდენობა: {dash_count}")
print(f"მხოლოდ ასოები და ციფრები: {is_alnum_without_dashes}")
print("-" * 40)

