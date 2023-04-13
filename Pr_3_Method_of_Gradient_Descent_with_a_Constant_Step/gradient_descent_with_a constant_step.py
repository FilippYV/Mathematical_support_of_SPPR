import math
from sympy import diff, symbols


def round_value(value):
    return round(value, 10)


def count_target_function(x, y):
    target_function = eval(function)
    return round_value(target_function)


def calculating_the_derivative():
    result_diff = []
    x, y = symbols('x y')
    target_function = eval(function)
    result_diff.append(str(target_function.diff(x)))
    result_diff.append(str(target_function.diff(y)))
    return result_diff


def count_grad_target_function(value_x, value_y):
    massive_derivative_calculating = []
    derivative = calculating_the_derivative()
    for index in range(2):
        y = value_y
        x = value_x
        print(f'Производная для {index} переменной: {derivative[index]}')
        relust = round_value(eval(f'{derivative[index]}'))
        print(f'Производная для {index} переменной = {relust}')
        massive_derivative_calculating.append(relust)
    return massive_derivative_calculating


def generate_new_coordinate(mass, grad, mass_h):
    print(mass)
    new_coordinate = [0, 0]
    for k in range(2):
        print(f'{round_value(mass[k] - mass_h[-1] * grad[k])} = {mass[k]} - {mass_h[-1]} * {grad[k]}')
        new_coordinate[k] = mass[k] - mass_h[-1] * grad[k]
        new_coordinate[k] = round_value(new_coordinate[k])
    print(f'Новая координата со значением [{new_coordinate[0]}; {new_coordinate[1]}]')
    new_coordinate.append(count_target_function(new_coordinate[0], new_coordinate[1]))
    print(f'Целевая функция: {new_coordinate[-1]}\n\n')
    return new_coordinate


def condition_end_search(mass, iteration):
    print(f'Проверим условие окончания поиска.\n'
          f'Для этого вычислим вектор градиента ∇f(x{len(mass) - 1}) в точке'
          f' x({len(mass) - 1})\n')
    mass_grad.append(count_grad_target_function(mass[-1][0], mass[-1][1]))
    print(f'Градиент функции ∇f(x{len(mass) - 1}): [{mass_grad[-1][0]}; {mass_grad[-1][1]}]\n')
    return find_norm_gradient_vector(mass, mass_grad[-1], e, iteration)


def find_norm_gradient_vector(mass, grad, e, iteration):
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
        return True


def changing_the_function(mass, new_coordinate, grad, h, iteration):
    if new_coordinate[-1] < mass[-1][-1]:
        print(f'Поскольку и f(x{len(mass)}) < f(x{len(mass) - 1})')
        print(f'Условие убывания функции выполнено.\n')
        mass.append(new_coordinate)
        return condition_end_search(mass, iteration)
    else:
        print(f'Поскольку и f(x{len(mass)}) > f(x{len(mass) - 1})')
        print(f'Условие убывания функции не выполнено.\n'
              f'Уменьшим величину шага h = h/2 = {mass_h[-1] / 2}\n')
        mass_h.append(mass_h[-1] / 2)
        print(f'Повторим вычисления координат точки x[{len(mass)}]')
        new_coordinate = generate_new_coordinate(mass[-1], mass_grad[-1], mass_h)
        print(f'Сравним f(x{len(mass) - 1}) и f (𝑥({len(mass)}))')
        return changing_the_function(mass, new_coordinate, mass_grad[-1], mass_h, iteration)


def table_output(mass):
    print('\nТаблица:')
    for i in range(len(mass)):
        print(f'Вершина №{i}: ', end='')
        for j in range(len(mass[i]) - 1):
            print(f'{round(mass[i][j], 10)} | ', end='')
        print(f'{round(mass[i][-1], 10)}', end='')
        print()
    print()

def out_graph(data):
    import matplotlib.pyplot as plt
    import numpy as np

    fig0 = plt.figure(figsize=(16, 9))
    ax0 = fig0.add_subplot(projection='3d')
    mass_x = []
    mass_y = []
    value_func = []
    for i in range(-(len(mass)), 0):
        mass_x.append(data[i][0])
        mass_y.append(data[i][1])
        value_func.append(data[i][-1])
    colors = np.arange(len(mass_x))
    col_1 = ax0.scatter(mass_x, mass_y, value_func, cmap="jet", c=colors)
    ax0.set_xlabel('Значения первой переменной х(1)')
    ax0.set_ylabel('Значения второй переменной х(2)')
    ax0.set_zlabel('Значения целевой функции f(x)')
    plt.colorbar(col_1)
    plt.savefig("static/plt_0.png")

    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot(projection='3d')
    mass_x = []
    mass_y = []
    value_func = []
    for i in range(-50, 0):
        mass_x.append(data[i][0])
        mass_y.append(data[i][1])
        value_func.append(data[i][-1])
    colors = np.arange(len(mass_x))
    col_1 = ax.scatter(mass_x, mass_y, value_func, cmap="jet", c=colors)
    ax.set_xlabel('Значения первой переменной х(1)')
    ax.set_ylabel('Значения второй переменной х(2)')
    ax.set_zlabel('Значения целевой функции f(x)')
    plt.colorbar(col_1)
    plt.savefig("static/plt_1.png")

    fig2 = plt.figure(figsize=(16, 9))
    ax_2 = fig2.add_subplot()
    mass_x = []
    mass_y = []
    value_func = []
    for i in range(-10, 0):
        mass_x.append(data[i][0])
        mass_y.append(data[i][1])
        value_func.append(data[i][-1])
    colors = np.arange(len(mass_x))
    col = ax_2.scatter(mass_x, mass_y, cmap="jet", c=colors)
    ax_2.set_xlabel('Значения первой переменной х(1)')
    ax_2.set_ylabel('Значения второй переменной х(2)')
    plt.colorbar(col)
    ax_2.grid()
    plt.savefig("static/plt_2.png")


if __name__ == '__main__':
    mass = [[9, 9]]
    n = len(mass[0])  # размерость
    h = 0.4  # начальная величина шага
    mass_h = [h]
    e = 0.001  # точность
    grad = 0
    mass_grad = []

    function = "10 * x ** 2 + 3 * x * y + y ** 2 + 10 * y"  # 7

    iteration = 0

    print(f'Вычислим значение целевой функции f(x{len(mass) - 1})\n')
    mass[-1].append(count_target_function(mass[-1][0], mass[-1][1]))
    print(f'Значение целевой функции f(x{len(mass) - 1}) = {mass[-1][2]}\n')
    print(f'Вычислим градиент ∇f(x{len(mass) - 1})')
    mass_grad.append(count_grad_target_function(mass[-1][0], mass[-1][1]))
    print(f'Градиент функции ∇f(x{len(mass) - 1}): [{mass_grad[-1][0]}; {mass_grad[-1][1]}]\n')

    # while iteration != 2:
    while iteration != -404:
        print('=' * 100)
        print('Итерация =', iteration)
        print('=' * 100)
        iteration += 1
        print(f'Найдем новую координату x[{len(mass)}]\n')
        new_coordinate = generate_new_coordinate(mass[-1], mass_grad[-1], mass_h)
        print(f'Сравним f(x{len(mass) - 1}) и f (𝑥({len(mass)}))')
        if changing_the_function(mass, new_coordinate, grad, h, iteration) is True:
            iteration = -404
    table_output(mass)
    out_graph(mass)