#
#
#
list_of_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']


# проверяем любой список на присутствие цифр signed и unsigned
def checking_for_a_number(user_any_list):
	count = 0
	total = 0
	signed_int_number = []
	for index in range(len(user_any_list)):
		temp_list = list(user_any_list[index])
		for value in range(len(temp_list)):
			if temp_list[value] == '-':
				if temp_list[value + 1].isdigit():
					count += 1
					signed_number = temp_list[value] + temp_list[value + 1]
					signed_int_number = ''.join(signed_number)
			elif not temp_list[value].isdigit():
				continue
			else:
				total += 1
	if total > 0:
		print(f'В данном списке: {user_any_list}', f'\nВсего чисел ', {total}, f'из них отрицательных {count}:', '(', signed_int_number, ')')
	else:
		print(f'В данном списке: {user_any_list}', '\nНет чисел!')


checking_for_a_number(list_of_employees)

for i in range(len(list_of_employees)):
	user_list = list_of_employees[i].split()
	print(f'Привет, {user_list[-1].title()}')
	user_list[-1] = user_list[-1].title()
	list_of_employees[i] = ' '.join(user_list)
print(f'Приводим список в порядок:\n{list_of_employees}')
