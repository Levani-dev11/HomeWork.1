swori_paroli = "python2024"
mcdeloba = 3

while mcdeloba > 0:
    paroli = input("შეიყვანე პაროლი: ")
    
    if paroli == "":
        mcdeloba -= 1
        print(f"არასწორი პაროლი. დარჩენილი მცდელობა: {mcdeloba}")
        continue 
        
    if paroli == swori_paroli:
        print("წვდომა დაშვებულია")
        break  
    else:
        mcdeloba -= 1
        print(f"არასწორი პაროლი. დარჩენილი მცდელობა: {mcdeloba}")

else:
    print("ანგარიში დაბლოკილია")
