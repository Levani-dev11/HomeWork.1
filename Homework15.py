# ნაწილი 1 — ქულების ჩაწერა; "w" ძველ შიგთავსს შლის.
def save_scores(path: str, scores: dict[str, int]) -> None:
    with open(path, "w", encoding="utf-8") as file:
        for name, score in scores.items():
            file.write(f"{name}:{score}\n")


# ნაწილი 2 — ახალი სტუდენტის დამატება ფაილის ბოლოში.
def add_score(path: str, name: str, score: int) -> None:
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{name}:{score}\n")


# ნაწილი 3 — ფაილის ხაზ-ხაზ წაკითხვა და დიქტის დაბრუნება.
def read_scores(path: str) -> dict[str, int]:
    scores = {}

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # დამატებითი: ცარიელი ხაზის გამოტოვება.
                if not line:
                    continue

                name, score = line.split(":")
                scores[name] = int(score)
    except FileNotFoundError:
        # დამატებითი: თუ ფაილი არ არსებობს, ვაბრუნებთ ცარიელ დიქტს.
        print("⚠ ფაილი ვერ მოიძებნა")
        return {}

    return scores


# დავალებაში მოცემული შემოწმება.
os.makedirs("data", exist_ok=True)

save_scores("data/scores.txt", {"ნინო": 92, "გიორგი": 78, "ანა": 85})
add_score("data/scores.txt", "დათო", 64)
add_score("data/scores.txt", "მარიამი", 97)

with open("data/scores.txt", encoding="utf-8") as file:
    print(file.read(), end="")

scores = read_scores("data/scores.txt")
print(scores)


# ნაწილი 4 — ქულების დამუშავება.
print(f"სტუდენტები: {len(scores)}")

if scores:
    average = round(sum(scores.values()) / len(scores), 1)
    print(f"საშუალო ქულა: {average}")

    best_student = max(scores, key=scores.get)
    print(f"საუკეთესო: {best_student} {scores[best_student]}")
else:
    print("ქულების სია ცარიელია")

with open("data/passed.txt", "w", encoding="utf-8") as file:
    for name, score in scores.items():
        if score >= 80:
            file.write(f"{name}\n")

passed = []
with open("data/passed.txt", "r", encoding="utf-8") as file:
    for line in file:
        passed.append(line.strip())

print(f"ჩააბარეს (80+): {passed}")
