print("=== სტუდენტის შეფასების სისტემა ===")

try:
    
    name_input = input("სტუდენტის სახელი: ")
    score_input = input("მიღებული ქულა: ")
    max_score_input = input("მაქსიმალური ქულა: ")
    
    student_name = name_input.strip()
    if not student_name:

        raise ValueError("❌ სახელი ცარიელი ვერ იქნება")
        

    initial = student_name[0]
    
    
    try:
        score = int(score_input)
        max_score = int(max_score_input)
    except ValueError:
        raise ValueError("❌ ქულები მთელი რიცხვებით ჩაწერეთ")
        
    
    if max_score == 0:
        raise ZeroDivisionError("❌ მაქსიმალური ქულა 0 ვერ იქნება")
        
    if score < 0 or score > max_score:
        raise ValueError("❌ ქულა არასწორ დიაპაზონშია")
        
    percent = (score / max_score) * 100
    
    if percent >= 91:
        grade = "A"
    elif percent >= 81:
        grade = "B"
    elif percent >= 71:
        grade = "C"
    elif percent >= 61:
        grade = "D"
    elif percent >= 51:
        grade = "E"
    elif percent >= 41:
        grade = "FX"
    else:
        grade = "F"

except ZeroDivisionError as ze:
    print(ze)

except ValueError as ve:
    print(ve)

else:
    print(f"✅ {initial}. {student_name} — {percent:.1f}% — შეფასება: {grade}")

finally:
    print("შეფასების სისტემამ მუშაობა დაასრულა")
