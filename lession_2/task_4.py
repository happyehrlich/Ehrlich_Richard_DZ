#
#
#
# прочитать про приведение чисел к двум разрядам
# деление числа в строке через запятую
from random import random


# получаем прайс лист
def get_random_list():
	price_list_random = []
	while len(price_list_random) < 20:
		price_list_random.append(round((random() * 89), 2))
	return price_list_random


#################################

price_list = get_random_list() # получаем прайс лист
print(id(price_list))
# делаем массив многомерным, не пересоздавая объекта
for i in range(len(price_list)):
	temp_var = str(price_list[i])
	temp_var = temp_var.split('.')
	price_list[i] = temp_var
print(price_list)

# дополняем одноразрядные цифры нулём, формируем правильный список цен
for index in range(len(price_list)):
	temp_some_num = price_list[index]
	for value in range(1, len(temp_some_num), 2):
		item = temp_some_num[value]
		if len(item) < 2:
			item = '0' + item
			temp_some_num[value] = item
	# temp_some_num[0] = f'{temp_some_num[0]} руб'
	# temp_some_num[1] = f'{temp_some_num[1]} коп'
	# temp_some_num = ' '.join(temp_some_num)
	temp_some_num = f'{temp_some_num[0]} руб {temp_some_num[1]} коп'
	price_list[index] = temp_some_num


# получаем cтроку из списка не пересоздавая объекта
# price_list = ', '.join(price_list)
while True:
	if len(price_list) > 1:
		temp_var_for_string = f'{price_list.pop(0)}, {price_list.pop(0)}'
		price_list.insert(0, temp_var_for_string)
	else:
		break
print(price_list)