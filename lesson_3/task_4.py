def thesaurus_adv(*args):
	user_dict = {}
	for value in args:
		temp_list = value.split(' ')
		key_dict = temp_list[1][0]
		if key_dict in user_dict.keys():
			continue
		else:
			list_values = get_value_dict(key_dict, args)
			user_dict[key_dict] = list_values
	return user_dict


def get_value_dict(ukey, ulist):
	just_list = []
	for value in ulist:
		temp_list = value.split(' ')
		if temp_list[1].startswith(ukey):
			just_list.append(value)
	final_value = thesaurus(just_list)
	return final_value


def thesaurus(args):
	user_dict = {}
	for value in args:
		temp_list = value.split(' ')
		first_sign = temp_list[0][0]
		if first_sign in user_dict.keys():
			continue
		next_list = list(filter(lambda item: item.startswith(first_sign), args))
		user_dict[first_sign] = next_list
	return user_dict


final_dict = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print('Входные данные: ', '"Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"')
print('Получаем словарь соблюдая условие: ', final_dict)
