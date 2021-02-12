
#some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#some_list = ['в', '5', 'часов', '17', '+5']
#some_list = ['в', '5', 'часов', '17', '+5']
some_list = ['5', 'часов', '+5']
some_list.reverse()
print(some_list)
for i in range(0, len(some_list)):
    temp_item = some_list[i]
    print('получаем первую строку: ' ,temp_item)
    temporary_list = list(temp_item)
    print('получаем временный список из строки: ' ,temporary_list)
    count = 0
    index_list = []
    general_index_list = []
    for index, value in enumerate(temporary_list):
        print('проверка индекса и значения: ', index, value)
        if value.isdigit():
            print('проверочный вывод, если значение является числом')
            count += 1
            index_list = str(index)
            print(index_list)
            general_index_list = index
        else:
            print('проверочный вывод, если значение является не числом')
            general_index_list = index
    if count == 1:
        qwe = index_list[0]
        print(type(qwe))
        print(type(temporary_list))
        temporary_list.insert(int(qwe), 0)
        print('проверочный вывод, temporary_list: ', temporary_list)
