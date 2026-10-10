
text = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."

text = text.lower().replace(",", "").replace(".", "")
counts = {}

for word in text.split():
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print(f"{word}: {count}")

most_frequent_word = ""
highest_count = 0

for word, count in counts.items():
    if count > highest_count:
        most_frequent_word = word
        highest_count = count

print(f"ყველაზე ხშირი: '{most_frequent_word}' ({highest_count}-ჯერ)")
print(f"სხვადასხვა სიტყვა: {len(counts)}")

print()