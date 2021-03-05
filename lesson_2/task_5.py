from random import random
from copy import copy


# получаем прайс лист
def get_random_list():
	price_list_random = []
	while len(price_list_random) < 20:
		price_list_random.append(round((random() * 89), 2))
	return price_list_random


def adding_a_zero(any_list):
	ending_num = ''
	for value in any_list:
		num = str(int(float(value) * 100))
		number = f"{int(value)} руб {str(list(num)[-2]) + str(list(num)[-1])} коп, "
		ending_num += number
	return ending_num


first_list = get_random_list()
print('Получаем новый список', '\nid:', id(first_list), first_list)

price_list = adding_a_zero(first_list)
print('Выводим цены согласно условию "А" :\n', price_list)

first_list.sort()
price_list = adding_a_zero(first_list)
print('Выводим цены согласно условию "B" :\n', price_list)

new_list = copy(first_list)
new_list.reverse()
price_list = adding_a_zero(new_list)
print('Выводим цены согласно условию "C" :\n', price_list)

price_list = adding_a_zero(first_list[-5:])
sorted(price_list)
print('Выводим цены согласно условию "D" :\n', price_list)
