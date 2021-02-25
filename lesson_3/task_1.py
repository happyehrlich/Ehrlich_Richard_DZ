def new_translate(eng_number, some_dict):
	print(some_dict.get(eng_number))


user_dictionary = dict(one='один', two='два', three='три', four='четыре', five='пять', six='шесть', seven='семь', eight='восемь', nine='девять', ten='десять')
print(type(user_dictionary), user_dictionary)

user_number = input('Введите ваше число на английском языке: ')
new_translate(user_number, user_dictionary)
