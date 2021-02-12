
some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


for i in range(0, len(some_list)):
    temp_item = some_list[i]
    temporary_list = list(temp_item)
    for i in range(0, len(temporary_list)):
        count += int(temporary_list[i].isdigit())
#    if 0 < count < 2: