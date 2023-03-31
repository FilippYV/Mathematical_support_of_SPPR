from sympy import diff, symbols, Symbol
from numpy.linalg import inv
import numpy as np
import math


def round_value(value):
    return round(value, 10)


def table_output(mass):
    print('\nТаблица:')
    for i in range(len(mass)):
        print(f'Вершина №{i}: ', end='')
        for j in range(len(mass[i]) - 1):
            print(f'{round(mass[i][j], 10)} | ', end='')
        print(f'{round(mass[i][-1], 10)}', end='')
        print()
    print()


def count_target_function(x, y):
    target_function = eval(function)
    return round_value(target_function)


def count_grad_target_function(value_x, value_y):
    massive_derivative_calculating = []
    derivative = calculating_the_derivative()
    y = value_y
    x = value_x
    print(f'x = {x}; y = {y}')
    for index in range(2):
        print(f'Производная для {index} переменной: {derivative[index]}')
        relust = round_value(eval(f'{derivative[index]}'))
        print(f'Производная для {index} переменной = {relust}')
        massive_derivative_calculating.append(relust)
    return massive_derivative_calculating


def calculating_the_derivative():
    result_diff = []
    x, y = symbols('x y')
    target_function = eval(function)
    result_diff.append(str(target_function.diff(x)))
    result_diff.append(str(target_function.diff(y)))
    return result_diff


def calculating_hesse_matrix(mass):
    hesse_matrix = []
    x, y = symbols('x y')
    target_function = eval(function)
    hesse_matrix.append([round_value(float(target_function.diff(x, x))),
                         round_value(float(target_function.diff(x, y)))])
    hesse_matrix.append([round_value(float(target_function.diff(y, x))),
                         round_value(float(target_function.diff(y, y)))])

    string_for_out_on_scren = f'Матрица Гессе для x({len(mass) - 1}) = '
    print(string_for_out_on_scren + f'| {hesse_matrix[0][0]}  {hesse_matrix[0][1]} |')
    print(f' ' * len(string_for_out_on_scren) + f'| {hesse_matrix[1][0]}  {hesse_matrix[1][1]} |\n')
    return hesse_matrix


def angular_minors_of_hesse_matrix(hesse_matrix):
    minor_1 = round_value(hesse_matrix[0][0])
    minor_2 = round_value(hesse_matrix[0][0] * hesse_matrix[1][1] - (hesse_matrix[0][1] * hesse_matrix[1][0]))

    print(f'Минор №1 = {minor_1}')
    print(f'Минор №2 = {hesse_matrix[0][0]} * {hesse_matrix[1][1]} -'
          f' ({hesse_matrix[0][1]} * {hesse_matrix[1][0]}) = {minor_2}')

    if minor_1 >= 0 and minor_2 >= 0:
        print('Так как знаки угловых миноров строго положительны,\n'
              'то согласно критерию Сильвестра матрица Гессе положительна определена.')
        return True
    else:
        print('страх')
        exit(123)
        return False


def determining_direction_descent(mass, hesse_matrix, grad):
    print(f'\nСледовательно, направление спуска определяем по формуле Ньютона')
    print(f'p({len(mass) - 1}) = - 𝐻−1(x({len(mass) - 1})) * 𝛻f(x({len(mass) - 1}))')
    matrix_grad = np.array([grad[0], grad[1]])
    mass_to_inv = np.array([[hesse_matrix[0][0], hesse_matrix[0][1]], [hesse_matrix[1][0], hesse_matrix[1][1]]])
    mass_to_inv = inv(mass_to_inv)
    for i in range(len(mass_to_inv)):
        for j in range(len(mass_to_inv[i])):
            mass_to_inv[i][j] = round_value(mass_to_inv[i][j])
    p = -(np.dot(mass_to_inv, matrix_grad))
    print(f'p({len(mass) - 1}) = | {p[0]}  {p[1]} |')
    return p


def calculating_coordinates_new_point(mass, p):
    matrix_start_point = np.array([mass[-1][0], mass[-1][1]])
    value = matrix_start_point + p
    new_coordinate = [round_value(value[0]), round_value(value[1]),
                      count_target_function(round_value(value[0]), round_value(value[1]))]

    print(f'Вычислим координаты точки x({len(mass)})')
    print(f'x({len(mass)}) = x({len(mass) - 1}) + p({len(mass) - 1}))')
    print(f'x({len(mass)}) = {matrix_start_point} − {p}')
    print(f'Новая координата со значением [{new_coordinate[0]}; {new_coordinate[1]}]')
    print(f'Целевая функция: {new_coordinate[-1]}\n\n')
    mass.append(new_coordinate)


def condition_end_search(mass):
    print(f'Проверим условие окончания поиска.\n'
          f'Для этого вычислим вектор градиента ∇f(x{len(mass) - 1}) в точке'
          f' x({len(mass) - 1})\n')
    mass_grad.append(count_grad_target_function(mass[-1][0], mass[-1][1]))
    print(f'Градиент функции ∇f(x{len(mass) - 1}): [{mass_grad[-1][0]}; {mass_grad[-1][1]}]\n')
    return find_norm_gradient_vector(mass, mass_grad[-1], e)


def find_norm_gradient_vector(mass, grad, e):
    print(f'Найдем норму вектора градиента x{len(mass) - 1}')
    norm = round_value(math.sqrt((grad[0] ** 2) + (grad[1] ** 2)))
    print(f'norm = √(({grad[0]}**2) + ({grad[1]} ** 2)) = {norm}')
    if norm >= e:
        print(f'norm = {norm} >= {e}')
        print('Итерации продолжаются.\n\n\n')
        return False
    else:
        print(f'norm = {norm} < {e}')
        print('Итерации завершаются.\n\n\n')
        return -404


def calculate_step(mass):
    pass


if __name__ == '__main__':
    # mass = [[-0.25, 0.5]]
    mass = [[9, 9]]
    # mass = [[0, 0]]
    n = len(mass[0])  # размерость
    mass_grad = []
    mass_p = []  # направление спуска
    e = 0.001  # точность
    iteration = 0

    function = "10 * x ** 2 + 3 * x * y + y ** 2 + 10 * y"  # 7
    # function = "(2.8 * y ** 2) + 1.9 * x + (2.7 * x ** 2) + 1.6 - 1.9 * y"
    # function = "x ** 2 - x * y + 3 * y ** 2 - x"

    print(f'Вычислим значение целевой функции f(x{len(mass) - 1})')
    mass[-1].append(count_target_function(mass[-1][0], mass[-1][1]))
    print(f'Значение целевой функции f(x{len(mass) - 1}) = {mass[-1][2]}\n')
    print(f'Вычислим градиент ∇f(x{len(mass) - 1})')
    mass_grad.append(count_grad_target_function(mass[-1][0], mass[-1][1]))
    print(f'Градиент функции ∇f(x{len(mass) - 1}): [{mass_grad[-1][0]}; {mass_grad[-1][1]}]\n')
    while iteration != -404:
        # while iteration != 3:
        print('=' * 100)
        print('Итерация =', iteration)
        print('=' * 100)

        iteration += 1
        print(f'Определим в формуле x({len(mass)}) = '
              f'x({len(mass) - 1}) + p({len(mass) - 1}) направление спуска p({len(mass) - 1}).')
        print(f'Для этого проведем анализ матрицы Гессе в точке x({len(mass) - 1}):H(x({len(mass) - 1}))')

        hesse_matrix = calculating_hesse_matrix(mass)  # матрица Гессе
        if angular_minors_of_hesse_matrix(hesse_matrix):
            p = determining_direction_descent(mass, hesse_matrix, mass_grad[-1])
            calculating_coordinates_new_point(mass, p)
            if condition_end_search(mass) == -404:
                iteration = -404
        else:
            calculate_step(mass)
    table_output(mass)
