import os


# ნაწილი 1 — ქულების ჩაწერა
def save_scores(path: str, scores: dict[str, int]) -> None:
    with open(path, "w", encoding="utf-8") as file:
        for name, score in scores.items():
            file.write(f"{name}:{score}\n")


# ნაწილი 2 — სტუდენტის დამატება
def add_score(path: str, name: str, score: int) -> None:
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{name}:{score}\n")


# ნაწილი 3 — ქულების წაკითხვა
def read_scores(path: str) -> dict[str, int]:
    scores = {}

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # ცარიელი ხაზები გამოვტოვოთ
                if not line:
                    continue

                name, score = line.split(":")
                scores[name] = int(score)

    except FileNotFoundError:
        print("⚠ ფაილი ვერ მოიძებნა")
        return {}

    return scores


# საქაღალდის შექმნა
os.makedirs("data", exist_ok=True)


# პირველი სამი ნაწილის შემოწმება
save_scores("data/scores.txt", {"ნინო": 92, "გიორგი": 78, "ანა": 85})
add_score("data/scores.txt", "დათო", 64)
add_score("data/scores.txt", "მარიამი", 97)

with open("data/scores.txt", encoding="utf-8") as file:
    print(file.read(), end="")

scores = read_scores("data/scores.txt")
print(scores)


# ნაწილი 4 — მონაცემების დამუშავება

# 1. სტუდენტების რაოდენობა
print(f"სტუდენტები: {len(scores)}")

if scores:
    # 2. საშუალო ქულა
    average = round(sum(scores.values()) / len(scores), 1)
    print(f"საშუალო ქულა: {average}")

    # 3. საუკეთესო სტუდენტი
    best_student = max(scores, key=scores.get)
    print(f"საუკეთესო: {best_student} {scores[best_student]}")
else:
    print("ქულების სია ცარიელია")


# 4. იმ სტუდენტების სახელების ჩაწერა, ვისაც 80 ან მეტი აქვს
with open("data/passed.txt", "w", encoding="utf-8") as file:
    for name, score in scores.items():
        if score >= 80:
            file.write(f"{name}\n")


# 5. სახელების წაკითხვა და სიად დაბეჭდვა
passed = []

with open("data/passed.txt", "r", encoding="utf-8") as file:
    for line in file:
        passed.append(line.strip())

print(f"ჩააბარეს (80+): {passed}")