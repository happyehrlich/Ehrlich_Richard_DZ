some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


def modifying_the_list(any_list):
	for i in range(len(any_list)):
		temporary_str = any_list[i][:]
		count = 0
		index_container = 0
		for index_variable, value in enumerate(temporary_str):
			if value.isdigit():
				count += 1
				index_container = index_variable
		if count == 1:
			any_list[i] = temporary_str[:index_container] + '0' + temporary_str[index_container] + temporary_str[index_container + 1:]
	return any_list

def insert_quotation_marks(total_number):
	next_index = 0
	count = 0
	for index in range(len(some_list)):
		for value in some_list[next_index]:
			if value.isnumeric():
				count = 1
		if count:
			some_list.insert(next_index, '"')
			some_list.insert(next_index + 2, '"')
			next_index += 3
			total_number += 1
		else:
			next_index += 1
		count = 0
	return total_number


def get_last_string(number_of_cycles):
	while True:
		try:
			where_char = some_list.index('"')
		except ValueError:
			where_char = 0
		any_str = ''
		if where_char:
			for _ in range(number_of_cycles):
				any_str += some_list.pop(where_char)
			some_list.insert(where_char, any_str)
		else:
			break
	last_string = ''
	for value in some_list:
		last_string += f'{value} '
	return last_string


print('Программе дан объект в виде списка:')
print(some_list, 'id:', id(some_list))

some_list = modifying_the_list(some_list)
print('Модифицируем список не создавая новый объект и не создавая новый список:')
print(some_list, 'id:', id(some_list))

total_numbers = insert_quotation_marks(0)
print(some_list, 'id:', id(some_list))

print('Получаем строку соблюдая условия:')
main_string = get_last_string(total_numbers)
print(main_string)