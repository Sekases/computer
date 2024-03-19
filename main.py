
memory = {
	'+': 'b0',
	'-': 'b1',
	'*': 'b10',
	'/': 'b11'
}

def ram(imn):
	ram = {
	'reg1': [0, 0, 0, 0, 0, 0, 0, 0],
	'reg2': [0, 0, 0, 0, 0, 0, 0, 0],
	'reg3': [0, 0, 0, 0, 0, 0, 0, 0]
}

def input_l():
	num1 = int(input('Enter number one: '))
	num2 = int(input('Enter number two: '))
	command = input('Enter command: ')
	return num1, num2, command

def transform(inp: tuple):
	for i in inp:
		if isinstance(i, int):
			pass # Перевести в двоичное представление. Проверить регистр 1, если пустой - сохранить в него. Если не пуст, сохранить в регистр 2
		else:
			pass # Сравнить с памятью. Сохранить в регистр 3, в бинарном представлении


print('Hello? This is computer of Kostya - KosKo! Pleas follow the instructions!') # Greeting(Приветствие)
temporary_storage = input_l() # Создание временного хранилища для чисел и команды
transform(temporary_storage) # Трансформация в двоичную систему
