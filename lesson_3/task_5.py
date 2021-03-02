import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def qwe(any_list):
	return random.choice(any_list)


def get_list_value(*args):
	temp_value = list(map(qwe, *args))
	return temp_value


def get_jokes(number_of_jokes, *args, flag=False):
	"""  """
	if flag and number_of_jokes > len(args[0]):
		print('Вы ввели не допустимое значение!')
	else:
		result_list = []
		for i in range(number_of_jokes):
			if flag:
				while True:
					temp_value = get_list_value(args)
					temp_str = ' '.join(str(i) for i in result_list)
					count = 0
					for value in temp_value:
						if temp_str.find(value) != -1:
							break
						count += 1
					if count == 3:
						result_list.append(f'{temp_value[0]} {temp_value[1]} {temp_value[2]}')
						break
			else:
				temp_value = get_list_value(args)
				result_list.append(f'{temp_value[0]} {temp_value[1]} {temp_value[2]}')
		return result_list


print(f"Условие: если в программе используються, только уникальнвые слова,\nто количество выдаваемых шуток неможет привышать длинну входного списка!: {len(nouns)}")
unique_words = input('Хотите ли вы видеть только уникальные слова? (Да/Нет): ')
quantity_of_jokes = input('Введите количество шуток, которое вы хотите увидеть: ')
if unique_words.lower() == 'да' and quantity_of_jokes.isdigit():
	result = get_jokes(int(quantity_of_jokes), nouns, adverbs, adjectives, flag=True)
	if result:
		print(result)
elif unique_words.lower() == 'нет' and quantity_of_jokes.isdigit():
	result = get_jokes(int(quantity_of_jokes), nouns, adverbs, adjectives)
	print(result)
else:
	print(unique_words)
	print('Не корректный ответ')
