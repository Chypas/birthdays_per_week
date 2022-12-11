from datetime import datetime, timedelta

users = [
    {"name": "Roman", "birthday": datetime(year=2022, month=12, day=9)},
    {"name": "Anna", "birthday": datetime(year=2022, month=12, day=10)},
    {"name": "Vasia", "birthday": datetime(year=2022, month=12, day=22)},
    {"name": "Ilona", "birthday": datetime(year=2022, month=12, day=11)},
    {"name": "Grigoriy", "birthday": datetime(year=2022, month=12, day=12)},
    {"name": "Alina", "birthday": datetime(year=2022, month=12, day=30)},
    {"name": "Sasha", "birthday": datetime(year=2022, month=12, day=14)},
    {"name": "Maksim", "birthday": datetime(year=2022, month=12, day=15)},
    {"name": "Vita", "birthday": datetime(year=2022, month=12, day=16)},
]


def get_birthdays_per_week(n):
    birthday_person = ""
    birthday_persons = []
    monday_w = []
    tuesday_w = []
    wednesday_w = []
    thursday_w = []
    friday_w = []
    interval = timedelta(days=+n)
    interval_of_birthday = datetime.now() + interval
    for l in users:
        if l["birthday"] < interval_of_birthday:
            birthday_person = l
            birthday_persons.append(birthday_person)
    for n in birthday_persons:
        #     print(n["birthday"].weekday())
        if n["birthday"].weekday() == 0:
            monday_w.append(n)
        elif n["birthday"].weekday() == 1:
            tuesday_w.append(n)
        elif n["birthday"].weekday() == 2:
            wednesday_w.append(n)
        elif n["birthday"].weekday() == 3:
            thursday_w.append(n)
        elif n["birthday"].weekday() == 4:
            friday_w.append(n)
        elif n["birthday"].weekday() == 5:
            monday_w.append(n)
        elif n["birthday"].weekday() == 6:
            monday_w.append(n)
    for dm in monday_w:
        mon_day = dm.get("name")
        birthday_person_m = f"Monday: {mon_day}" 
        print(birthday_person_m)
    for dt in tuesday_w:
        tu_day = dt.get("name")
        birthday_person_t = f"Tuesday: {tu_day}" 
        print(birthday_person_t)
    for dw in wednesday_w:
        wed_day = dw.get("name")
        birthday_person_w = f"Wednesday: {wed_day}" 
        print(birthday_person_w)    
    for dth in thursday_w:
        th_day = dth.get("name")
        birthday_person_th = f"Thursday: {th_day}" 
        print(birthday_person_th)
    for df in friday_w:
        fr_day = df.get("name")
        birthday_person_f = f"Friday: {fr_day}" 
        print(birthday_person_f)
        

get_birthdays_per_week(7)
