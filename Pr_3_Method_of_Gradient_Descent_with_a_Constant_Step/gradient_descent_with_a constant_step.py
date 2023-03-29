import math
from sympy import diff, Symbol


def round_value(value):
    return round(value, 6)


def count_target_function(x, y):
    # target_function = 10 * x ** 2 + 3 * x * y + y ** 2 + 10 * y  # 7
    # target_function = x**2 - x*y + 3*y**2-x
    target_function = 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y
    return round_value(target_function)


def calculating_the_derivative_for_x():
    x = Symbol('x')
    y = 0
    target_function = 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y
    result_diff = str(target_function.diff(x))
    return result_diff


def calculating_the_derivative_for_y():
    y = Symbol('y')
    x = 0
    target_function = 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y
    result_diff = str(target_function.diff(y))
    return result_diff


def count_grad_target_function(value_x, value_y):
    massive_derivative_calculating = []
    for index in range(2):
        if index == 0:
            derivative = calculating_the_derivative_for_x()
            x = value_x
        elif index == 1:
            derivative = calculating_the_derivative_for_y()
            y = value_y
        print(f'Производная для {index} переменной: {derivative}')
        relust = round_value(eval(f'{derivative}'))
        print(f'Производная для {index} переменной равна {relust}')
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


if __name__ == '__main__':
    mass = [[1, 1]]
    n = len(mass[0])  # размерость
    h = 0.4  # начальная величина шага
    mass_h = [h]
    count_h = 0
    e = 0.1  # точность
    symbols = [Symbol('x'), Symbol('y')]
    grad = 0
    mass_grad = []

    iteration = 0

    print(f'Вычислим значение целевой функции f(x{len(mass) - 1})\n')
    mass[-1].append(count_target_function(mass[-1][0], mass[-1][1]))
    print(f'Значение целевой функции f(x{len(mass) - 1}) = {mass[-1][2]}\n')
    print(f'Вычислим градиент ∇f(x{len(mass) - 1})')
    mass_grad.append(count_grad_target_function(mass[-1][0], mass[-1][1]))
    print(f'Градиент функции ∇f(x{len(mass) - 1}): [{mass_grad[-1][0]}; {mass_grad[-1][1]}]\n')

    # while iteration != 2:
    while iteration is not True:
        print('=' * 100)
        print('Итерация =', iteration)
        print('=' * 100)
        iteration += 1
        print(f'Найдем новую координату x[{len(mass)}]\n')
        new_coordinate = generate_new_coordinate(mass[-1], mass_grad[-1], mass_h)
        print(f'Сравним f(x{len(mass) - 1}) и f (𝑥({len(mass)}))')
        if changing_the_function(mass, new_coordinate, grad, h, iteration) is True:
            iteration = True
