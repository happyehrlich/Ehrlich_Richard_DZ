# <-- СТАРТ БЛОКА ОБЪЯВЛЕНИЙ --> 
def get_total(count_list, temp_sum, total):
    for i in range(0, len(number_cube)):    # обработка каждого значения списка
        temp_number = number_cube[i]        # получение значения по индексу
        temp_list = []
        for i in str(temp_number):          # разбираем число на символы
            temp_list.append(i)
        for i in range(0, len(temp_list)):  # получаем сумму значений списка
            temp_sum += int(temp_list[i])
        if temp_sum % 7 == 0:               # проверяем подхолит ли сумма под условия 
            count_list.append(temp_sum)     # для присваивания в список
        temp_sum = 0
    for i in range(0, len(count_list)):     # получаем ответ по заданию
        total += count_list[i]
    print(total)


number_cube = []
count_list = []
temp_sum = 0
total = 0
# <-- КОНЕЦ БЛОКА ОБЪЯВЛЕНИЙ -->

# Наполняем список number_cube[] согласно условию в задании
for i in range(1, 1001):
    if i % 2 != 0:
        number_cube.append(i ** 3)

get_total(count_list, temp_sum, total)

# Обнуление значений перед использованием
count_list.clear()
temp_sum = 0
total = 0

# Изменяем список number_cube[] согласно условию в задании
for i in range(0, len(number_cube)):
    number_cube[i] = number_cube[i] + 17

get_total(count_list, temp_sum, total)