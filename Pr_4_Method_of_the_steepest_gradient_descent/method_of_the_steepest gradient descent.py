from sympy import diff, symbols, Symbol
import math


def round_value(value):
    return round(value, 10)


def count_target_function(x, y):
    target_function = 10 * x ** 2 + 3 * x * y + y ** 2 + 10 * y  # 7
    # target_function = x**2 - x*y + 3*y**2-x
    # target_function = 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y
    # target_function = 2 * x ** 2 + x * y + y ** 2
    return round_value(target_function)


def transform_for_h():
    # target_function = '2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y'
    target_function = '10 * x ** 2 + 3 * x * y + y ** 2 + 10 * y'  # 7
    target_function = target_function.replace("x", "h")
    target_function = target_function.replace("y", "h")
    print(target_function)


def calculating_the_derivative_for():
    result_diff = []
    x, y = symbols('x y')
    target_function = 10 * x ** 2 + 3 * x * y + y ** 2 + 10 * y  # 7
    # target_function = (2.8 * y ** 2) + 1.9 * x + (2.7 * x ** 2) + 1.6 - 1.9 * y
    # target_function = 2 * x ** 2 + x * y + y ** 2
    result_diff.append(str(target_function.diff(x)))
    result_diff.append(str(target_function.diff(y)))
    return result_diff


def count_grad_target_function(value_x, value_y):
    massive_derivative_calculating = []
    derivative = calculating_the_derivative_for()
    for index in range(2):
        y = value_y
        x = value_x
        print(f'Производная для {index} переменной: {derivative[index]}')
        relust = round_value(eval(f'{derivative[index]}'))
        print(f'Производная для {index} переменной = {relust}')
        massive_derivative_calculating.append(relust)
    return massive_derivative_calculating


def derivative_for_h():
    result_diff = []
    x, y = symbols('x y')
    target_function = 10 * x ** 2 + 3 * x * y + y ** 2 + 10 * y  # 7
    # target_function = (2.8 * y ** 2) + 1.9 * x + (2.7 * x ** 2) + 1.6 - 1.9 * y
    # target_function = 2 * x ** 2 + x * y + y ** 2
    target_function = str(target_function)
    return target_function


def calculating_the_derivative_for_h(func):
    h = Symbol('h')
    print(func)
    target_function = eval(func)
    print(target_function)
    result_diff = str(target_function.diff(h))
    result_diff = result_diff.replace('- ', '-')
    result_diff = result_diff.replace('+ ', '+')
    result_diff = result_diff.split(' ')
    h = 0
    value = 0
    for i in range(len(result_diff)):
        if result_diff[i][-1].isalpha():
            h = float(result_diff[i].replace('*h', ''))
        else:
            value = float(result_diff[i])
    print(value, 'value')
    print(h, 'h')
    return value, h


def count_h(value_x, value_y):
    massive_derivative_calculating = []
    derivative = derivative_for_h()
    print(derivative)
    print(value_x)
    print(value_y)
    derivative = derivative.replace('x', value_x)
    derivative = derivative.replace('y', value_y)
    print('\nchange ====', derivative, )
    value, h = calculating_the_derivative_for_h(derivative)
    if h >= 0:
        h = - value / h
    else:
        h = value / h
    h = round_value(h)
    print(h)
    if h > 0:
        return h
    else:
        return False


def generate_new_coordinate(mass, grad):
    print(mass)
    new_coordinate = [0, 0]
    for k in range(2):
        # print(f'{mass[k]} {grad[k]} = {mass[k]}  {grad[k]}')
        new_coordinate[k] = f'({mass[-1][k]} - h * {grad[k]})'
    print(new_coordinate)
    h = count_h(new_coordinate[0], new_coordinate[1])
    if h is not False:
        for k in range(2):
            print(f'x[{len(mass)}] = {mass[-1][k]} - {h} * {grad[k]}')
            new_coordinate[k] = mass[-1][k] - h * grad[k]
    else:
        exit(707)
    print(f'Новая координата со значением [{new_coordinate[0]}; {new_coordinate[1]}]')
    new_coordinate.append(count_target_function(new_coordinate[0], new_coordinate[1]))
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
        return iteration
    else:
        print(f'norm = {norm} < {e}')
        print('Итерации завершаются.\n\n\n')
        return False


def table_output(mass):
    print('\nТаблица:')
    for i in range(len(mass)):
        print(f'Вершина №{i}: ', end='')
        for j in range(len(mass[i]) - 1):
            print(f'{round(mass[i][j], 10)} | ', end='')
        print(f'{round(mass[i][-1], 10)}', end='')
        print()
    print()


if __name__ == '__main__':
    mass = [[9, 9]]
    n = len(mass[0])  # размерость
    mass_grad = []
    e = 0.1  # точность
    iteration = 0

    print(f'Вычислим значение целевой функции f(x{len(mass) - 1})\n')
    mass[-1].append(count_target_function(mass[-1][0], mass[-1][1]))
    print(f'Значение целевой функции f(x{len(mass) - 1}) = {mass[-1][2]}\n')
    print(f'Вычислим градиент ∇f(x{len(mass) - 1})')
    mass_grad.append(count_grad_target_function(mass[-1][0], mass[-1][1]))
    print(f'Градиент функции ∇f(x{len(mass) - 1}): [{mass_grad[-1][0]}; {mass_grad[-1][1]}]\n')
    while iteration != False:
        print('=' * 100)
        print('Итерация =', iteration)
        print('=' * 100)
        iteration += 1
        print(f'Найдем новую координату x[{len(mass)}]\n')
        new_coordinate = generate_new_coordinate(mass, mass_grad[-1])
        iteration = condition_end_search(mass)
    table_output(mass)
