#
#
#
some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


#
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


#

get_modify_list()
print(some_list)
print(len(some_list))
total_index = 0
for index in range(len(some_list)):
    temp_item1 = some_list[total_index]
    temporary_list1 = list(temp_item1)
    count1 = [value for value in temporary_list1 if value.isnumeric()]
    print(index + 1, total_index, count1)
    if count1:
        some_list.insert(total_index, '"')
        some_list.insert(total_index + 2, '"')
        print(some_list)
        total_index += 3
    else:
        total_index += 1

# найти индексы кавычек и склеить по срезу с числом
# потом пробелом склеить остальную строку
print(some_list.index('"'))
