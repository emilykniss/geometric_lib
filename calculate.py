import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
        
        ''' Вычисляет значение указанной функции для заданной фигуры
            с переданным размером.

        Аргументы:
        fig(str): Название фигуры(пример: 'circle', 'square')
        func(str): Название функции(пример: 'perimeter', 'area')
        size(list): Размер фигуры, передаваемые в функцию(пример: [радиус] для круга)

        Возвращает:
        None: Выводит результат на экран.
        '''
        
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



