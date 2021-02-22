from random import random


# получаем прайс лист
def get_random_list():
	price_list_random = []
	while len(price_list_random) < 20:
		price_list_random.append(round((random() * 89), 2))
	return price_list_random


#################################


def get_price_list(price_list):
	# делаем массив многомерным, не пересоздавая объекта
	for i in range(len(price_list)):
		temp_var = str(price_list[i])
		temp_var = temp_var.split('.')
		price_list[i] = temp_var

	# дополняем одноразрядные цифры нулём, формируем правильный список цен
	index: int
	for index in range(len(price_list)):
		some_numbers = price_list[index]
		for value in range(1, len(some_numbers), 2):
			item = some_numbers[value]
			if len(item) < 2:
				item = '0' + item
				some_numbers[value] = item
		some_numbers = f'{some_numbers[0]} руб {some_numbers[1]} коп'
		price_list[index] = some_numbers

	# получаем cтроку из списка не пересоздавая объекта
	while True:
		if len(price_list) > 1:
			temp_var_for_string = f'{price_list.pop(0)}, {price_list.pop(0)}'
			price_list.insert(0, temp_var_for_string)
		else:
			break
	return price_list


#################################################
print('получаем новый список и объект:')
get_random_number: list
get_random_number = get_random_list()
print(get_random_number)
print(id(get_random_number))

print('\nполучаем изменённый список цен по первому условию, но не изменяя объект:')
ready_price_list = get_price_list(get_random_number)
print(ready_price_list)
print(id(ready_price_list))

print('#################################################')
#
# print('\nберём объект из первого условия и сортируем по второму условию:')
# get_random_number = get_random_number[0]
# print(get_random_number)
# print(id(get_random_number))

# print('\nполучаем изменённый список цен по второму условию, не изменяя объект:')
# ready_price_list = get_price_list(get_random_number)
# print(ready_price_list)
# print(id(ready_price_list))

print('#################################################')
