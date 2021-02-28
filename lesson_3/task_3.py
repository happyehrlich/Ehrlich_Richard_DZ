def thesaurus(*args):
	user_dict = {}
	for value in args:
		first_sign = value[0]
		print(type(first_sign))
		if first_sign in user_dict.keys():
			continue
		next_list = list(filter(lambda item: item.startswith(first_sign), args))
		user_dict[first_sign] = next_list
	return user_dict


def sorted_dict_keys(some_dict):
	temp_dict = {}
	list_keys = list(some_dict.keys())
	list_keys.sort()
	for key in list_keys:
		temp_dict[key] = some_dict[key]
	return temp_dict


any_dict = thesaurus("Петр", "Иван", "Мария", "Илья")
print('Получаем словарь из списка:', any_dict)
sorted_dict = sorted_dict_keys(any_dict)
print('Отсортированный словарь:', sorted_dict)
