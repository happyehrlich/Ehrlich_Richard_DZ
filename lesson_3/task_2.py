def new_translate_adv(eng_number, some_dict):
	if eng_number.istitle():
		user_value = some_dict.get(eng_number.lower())
		print(user_value.title())
	else:
		print(some_dict.get(eng_number))


user_dictionary = dict(one='один', two='два', three='три', four='четыре', five='пять', six='шесть', seven='семь', eight='восемь', nine='девять', ten='десять')

user_number = input('Введите ваше число на английском языке: ')
new_translate_adv(user_number, user_dictionary)
