#
#
#
some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


#
def get_modofid_list():
    for i in range(len(some_list)):
        temp_item = some_list[i]
        temporary_list = list(temp_item)
        count = 0
        index_list = []
        general_index_list = []
        for index, value in enumerate(temporary_list):
            if value.isdigit():
                count += 1
                index_list = str(index)
                general_index_list = index
            else:
                general_index_list = index

        if count == 1:
            qwe = index_list[0]
            temporary_list.insert(int(qwe), '0')
            char_for_join = ''
            output1 = char_for_join.join(temporary_list)
            some_list[i] = output1


#

get_modofid_list()
print(some_list)
