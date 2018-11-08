from datetime import date

today = date.today()
born_date = input("Please enter your birthdate 'yyyy-mm-dd' ")
split_born = born_date.split("-")
born_day = int(split_born[2])
born_month = int(split_born[1])
born_year = int(split_born[0])
total = today.year - born_year - ((today.month, today.day) < (born_month, born_day))

if total >= 18:
    print("Congrats you are old enough")
elif total > 15 < 18 :
    print("Almost There")

else:
    print("Sorry your to young to join the party.")