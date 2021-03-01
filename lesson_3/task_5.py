import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_random_word(any_list):
	return random.choice(any_list)



quantity_jokes = int(input('Введите колличество шуток, которое вы хотите увидеть: '))
