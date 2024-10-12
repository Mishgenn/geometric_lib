import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	'''
	Эта функция, написанная на Python, выполняет вычисления для различных геометрических фигур, используя определенные функции для этих фигур.
	Вот что происходит в каждом шаге:
	1. **Проверка входных данных**: Функция `calc` принимает три аргумента: `fig` (название фигуры), `func` (название функции) и `size` (размеры фигуры). 
	В начале проверяется, что `fig` находится в списке доступных фигур (`figs`), а `func` — в списке доступных функций (`funcs`). 
	2. **Вычисление результата
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



