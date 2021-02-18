#
#
#
some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# функция добавляет "0" перед числом, если оно состоит из одного разряда
def get_modify_list():
    for i in range(len(some_list)):
        temp_item = some_list[i]
        temporary_list = list(temp_item)
        count = 0
        index_list = []
        for index_variable, value in enumerate(temporary_list):
            if value.isdigit():
                count += 1
                index_list = str(index_variable)

        if count == 1:
            qwe = index_list[0]
            temporary_list.insert(int(qwe), '0')
            char_for_join = ''
            output1 = char_for_join.join(temporary_list)
            some_list[i] = output1


# функция вставляем ковычки до и после числа
def inserting_a_quotation_mark_character():
    total_index = 0  # переменная для контроля шага итерации после увеличения длинны массива (чтобы не застревал на ковычках)
    for index in range(len(some_list)):
        temp_item1 = some_list[total_index]
        temporary_list1 = list(temp_item1)
        count1 = [value for value in temporary_list1 if value.isnumeric()]
        if count1:
            some_list.insert(total_index, '"')
            some_list.insert(total_index + 2, '"')
            total_index += 3
        else:
            total_index += 1


# функция get_any_symbol получает первую пару ковычек с начала списка
def get_any_character(any_list, any_symbol):
    symbol_list = []
    counter = 0
    for i in range(len(any_list)):
        if any_list[i] == any_symbol:
            symbol_list.append(i)
            counter += 1
        if counter == 2:
            break
    return symbol_list


print("\nПрограмме дан список: ", some_list)  # показываем не изменённый список
get_modify_list()  # Вызов модификации - первый этап
print("По условию, мы добавляем '0' к числам из этого списка, у которых один разряд", "\n:", some_list, '\n')  # показываем изменённый список
inserting_a_quotation_mark_character()  # Вызов модификации - второй этап
print("Далее обрамляем каждое число в ковычки: ")  # показываем изменённый список

while some_list.count('"') > 0:
    pair_symbol = get_any_character(some_list, '"')
    list_reload = []
    for i in range(pair_symbol[0], pair_symbol[-1] + 1):
        list_reload += some_list.pop(pair_symbol[0])
    list_reload = ''.join(list_reload)
    some_list.insert(pair_symbol[0], list_reload)
print(some_list, '\n')

some_list = ' '.join(some_list)  # Получаем из списка строку
print('Получаем из списка строку:', some_list)
