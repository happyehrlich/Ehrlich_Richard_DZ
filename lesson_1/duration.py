# Программа конвертации секунд в другие единицы времени

user_duration = int(input("Введите промежуток времени в секундах: "))

one_minute: int = 60
one_hour = one_minute * 60
one_day = one_hour * 24
one_week = one_day * 7
one_month = one_day * 31
one_year = one_month * 12

temp_sec = (((((user_duration % one_year) % one_month) % one_week) % one_day) % one_hour) % one_minute
temp_min = (((((user_duration % one_year) % one_month) % one_week) % one_day) % one_hour) // one_minute
temp_hour = ((((user_duration % one_year) % one_month) % one_week) % one_day) // one_hour
temp_day = (((user_duration % one_year) % one_month) % one_week) // one_day
temp_week = ((user_duration % one_year) % one_month) // one_week
temp_month = (user_duration % one_year) // one_month
temp_year = user_duration // one_year

if user_duration < one_minute:
    print("Промежуток времени длится: {} sec".format(user_duration))
elif user_duration < one_hour:
    print("Промежуток времени длится: {} min. {} sec.".format(temp_min, temp_sec))
elif user_duration < one_day:
    print("Промежуток времени длится: {} h. {} min. {} sec.".format(temp_hour, temp_min, temp_sec))
elif user_duration < one_month:
    print("Промежуток времени длится: {} w. {} d. {} h. {} min. {} sec.".format(temp_week, temp_day, temp_hour, temp_min, temp_sec))
elif user_duration < one_year:
    print("Промежуток времени длится: {} m. {} w. {} d. {} h. {} min. {} sec.".format(temp_month, temp_week, temp_day, temp_hour, temp_min, temp_sec))
elif user_duration > one_year:
    print("Промежуток времени длится: {} y. {} m. {} w. {} d. {} h. {} min. {} sec.".format(temp_year, temp_month, temp_week, temp_day, temp_hour, temp_min, temp_sec))
