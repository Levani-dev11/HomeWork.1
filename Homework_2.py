seconds = int(input("გთხოვთ შეიყვანოთ წამების რაოდენობა: "))
hours = seconds // 3600
seconds2 = seconds % 3600
minutes = seconds2 // 60
final_seconds = seconds2 % 60
print(hours, "საათი", minutes, "წუთი" , final_seconds, "წამი")
