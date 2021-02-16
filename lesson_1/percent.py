version_1 = [[2, 3, 4], 'процента']
version_2 = [[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 'процентов']

user_number = input("Введите колличество процентов от 1 до 20: ")

if user_number.isdigit():
    user_number = int(user_number)
    if 0 < user_number < 21:
        if user_number == 1:
            print("Вы ввели один процент")
        elif user_number in version_1[0]:
            print("Вы ввели {} {} ".format(user_number, version_1[1]))
        elif user_number in version_2[0]:
            print("Вы ввели {} {} ".format(user_number, version_2[1]))
    else:
        print("Вы ввели не допустимое значение")
else:
    print("Это не число")

