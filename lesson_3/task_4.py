def thesaurus_adv(*args):
	user_dict = {}
	count = 0
	total = 0
	for value in args:
		print('\nполучили из args:', value, '\n')
		temp_list = value.split(' ')
		key_dict = temp_list[1][0]
		print(key_dict, ' ===  новый ключ!!!')
		list_values = ''
		for item in args:
			_i = item.split(' ')
			print(_i)
			if _i[1].startswith(key_dict):
				list_values += f'{item}, '
				print(key_dict, list_values, '\nНАПОЛНЕНИЕ СТРОКИ')
			count += 1
			print('ИТЕРАЦИЯ вложенного цикла НОМЕР:', count, '\n')
		if key_dict in user_dict.keys():
			break
		else:
			user_dict[key_dict] = list_values
		print('\n===конец внешнего цикла===')
		count = 0  # обнуляем счётчик вложенного цикла
		total += 1
		print('===ИТЕРАЦИЯ внешнего цикла НОМЕР:', total, '===')


thesaurus_adv('Петр Алексеев', 'Иван Сергеев', 'Инна Серова', 'Илья Иванов', 'Анна Савельева')
