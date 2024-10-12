import math


def area(r):
    '''
    Аргумент: Функция принимает один параметр — радиус круга.
    Формула: Она использует математическую формулу для площади круга.
    π — это константа, представляющая отношение длины окружности к её диаметру (примерно 3.14).
    Возвращаемое значение: Функция вычисляет площадь и возвращает это значение.
    Таким образом, вызвав эту функцию с заданным радиусом, вы получите площадь круга с этим радиусом. Например, если радиус равен 5, функция вернет значение около 78.54.
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Аргумент: Функция принимает один параметр — радиус круга.
    Формула: Используется математическая формула для вычисления периметра круга: 
    π — это константа, представляющая отношение длины окружности к её диаметру.
    Возвращаемое значение: Функция вычисляет длину окружности и возвращает это значение.
    Таким образом, вызвав эту функцию с заданным радиусом, вы получите длину окружности круга с этим радиусом. Например, если радиус равен 5, функция вернет значение около 31.42.
    '''
    return 2 * math.pi * r

