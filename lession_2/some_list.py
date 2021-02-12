
#some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
some_list = ['в', '5', 'часов', '17', '+5']

for i in range(0, len(some_list)):
    temp_item = some_list[i]
    print('получаем первую строку: ' ,temp_item)
    temporary_list = list(temp_item)
    print('получаем временный список из строки: ' ,temporary_list)
    count = None
    index_list = []
    general_index_list = []
    for index, value in enumerate(temporary_list):
        if value.isdigit():
            count += 1
            index_list = index
            general_index_list = index
        else:
            general_index_list = index
    if count == 1:
        temporary_list.insert(temporary_list[0], 0)