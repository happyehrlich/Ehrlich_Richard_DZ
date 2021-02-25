def thesaurus_adv(*args):
	user_dict = {}
	for value in args:
		print(type(args))
		first_list = value.split(' ')
		first_sign = first_list[-1][0]
		print(first_sign, type(first_sign))
		if first_sign in user_dict.keys():
			break
		next_list = list(filter(lambda item:item.startswith(first_sign)))
		print(next_list)





def sorted_dict_keys(some_dict):
	temp_dict = {}
	list_keys = list(some_dict.keys())
	list_keys.sort()
	for key in list_keys:
		temp_dict[key] = some_dict[key]
	return temp_dict


any_dict = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# print('Получаем словарь из списка:', any_dict)
# sorted_dict = sorted_dict_keys(any_dict)
# print('Отсортированный словарь:', sorted_dict)
