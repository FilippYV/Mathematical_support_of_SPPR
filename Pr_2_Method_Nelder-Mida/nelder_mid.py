import math


def calculate_increments(mass, m, n):
    print(mass, m, n)
    d1 = round(((math.sqrt(n + 1) - 1) / (n * math.sqrt(2))) * m, 5)
    print(f'd1 = ({(math.sqrt(n + 1) - 1)} / {(n * math.sqrt(2))}) * {m}')
    print('d1 =', d1, '\n')

    d2 = round(((math.sqrt(n + 1) + n - 1) / (n * math.sqrt(2))) * m, 5)
    print(f'd2 = ({(math.sqrt(n + 1) + n - 1)} / {(n * math.sqrt(2))}) * {m}')
    print('d2 =', d2, '\n')

    new_x_1 = [mass[-1][0] + d1, mass[-1][1] + d2]
    print(f'new_x = [{mass[-1][0]} + {d1}; {mass[-1][1]} + {d2}]')
    print('new_x =', new_x_1, '\n')
    new_x_2 = [mass[-1][0] + d2, mass[-1][1] + d1]
    print(f'new_x = [{mass[-1][0]} + {d2}; {mass[-1][1]} + {d1}]')
    print('new_x =', new_x_2, '\n')
    mass.append(new_x_1)
    mass.append(new_x_2)
    # exit(69)


def table_output(mass):
    print('\nТаблица:')
    for i in range(len(mass)):
        print(f'Вершина №{i}: ', end='')
        for j in range(len(mass[i]) - 1):
            print(f'{round(mass[i][j], 5)} | ', end='')
        print(f'{round(mass[i][-1], 5)}', end='')
        print()
    print()


def count_target_function(x, y):
    # target_function = 10 * x ** 2 + 3 * x * y + y ** 2 + 10 * y  # 7
    # target_function = 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y
    # target_function = x ** 2 - x * y + 3 * y ** 2 - x
    target_function = 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y
    target_function = round(target_function, 5)
    return target_function


def determination_of_min_mean_max(min_mean_max, mass, mass_maximum):
    print(mass_maximum, 'mass_maximum')
    massive_for_search = []
    for i in range(len(mass)):
        if i not in mass_maximum:
            massive_for_search.append([mass[i][-1], i])
    maximum = [-1000000, 123]
    minimal = [1000000, 123]
    for i in range(len(massive_for_search)):
        if massive_for_search[i][0] > maximum[0]:
            maximum = massive_for_search[i]
        if massive_for_search[i][0] < minimal[0]:
            minimal = massive_for_search[i]
    mean = 0
    for i in range(len(massive_for_search)):
        if massive_for_search[i][1] != minimal[1] and massive_for_search[i][1] != maximum[1]:
            mean = massive_for_search[i]
    for i in range(len(min_mean_max)):
        if i == 0:
            min_mean_max[i] = minimal
        elif i == 1:
            min_mean_max[i] = mean
        elif i == 2:
            min_mean_max[i] = maximum
    print(min_mean_max)


def maximum_value_function(mass, mass_maximum):
    maximum = [-99999999, 0]
    for i in range(len(mass)):
        if mass[i][-1] > maximum[0] and i not in mass_maximum:
            maximum = [mass[i][-1], i]
    print(f'Максимум функции = {round(maximum[0], 5)}, номер вершины = {maximum[1]}')
    print()
    mass_maximum.append(maximum[1])


def center_of_gravity(mass, mass_maximum):
    x_center = [0, 0]
    for i in range(len(mass)):
        if i not in mass_maximum:
            x_center[0] += mass[i][0]
            x_center[1] += mass[i][1]
    for i in range(len(x_center)):
        x_center[i] *= 0.5
    for i in range(len(x_center)):
        x_center[i] = round(x_center[i], 5)
    print(f'Центер тяжести = [{round(x_center[0], 5)}, {round(x_center[1], 5)}]')
    print()
    return x_center


def finding_coordinates_reflected_vertex(mass, mass_maximum, center_g, min_mean_max):
    new_coordinate = []
    for i in range(n):
        new_coordinate.append(round(2 * center_g[i] - mass[min_mean_max[-1][1]][i], 5))
    print(f'Новые координаты = [{round(new_coordinate[0], 3)}; {round(new_coordinate[1], 5)}]')
    target_func = count_target_function(new_coordinate[0], new_coordinate[1])
    print('Целевая функция =', target_func, '\n')
    new_coordinate.append(target_func)
    return new_coordinate


def condition_fulfillment(mass, mass_maximum, min_mean_max, new_coordinate):
    if min_mean_max[1][0] < new_coordinate[-1] < min_mean_max[-1][0]:
        print(f'\nТак как выполняется условие:')
        print(f'x{min_mean_max[1][1]} < x{len(mass) - 1} < x{min_mean_max[-1][1]}')
        print(f'x{min_mean_max[1][0]} < {new_coordinate[-1]} < {min_mean_max[-1][0]}')
        mass_maximum.append(len(mass) - 1)
        return True
    else:
        print(f'\nУсловие не выполняется:')
        print(f'x{min_mean_max[1][1]} <! x{len(mass) - 1} <! x{min_mean_max[-1][1]}')
        print(f'x{min_mean_max[1][0]} <! x{new_coordinate[-1]} <! x{min_mean_max[-1][0]}')
        return False


def condition_end_search(mass, mass_maximum, n, e):
    x_center = [0, 0]
    # print(mass_maximum)
    for i in range(len(mass)):
        if i not in mass_maximum:
            x_center[0] += mass[i][0]
            x_center[1] += mass[i][1]
    for i in range(len(x_center)):
        x_center[i] = round(x_center[i] / 3, 5)
    x_center.append(count_target_function(x_center[0], x_center[1]))
    print(f'Центер тяжести = [{x_center[0]}, {x_center[1]}]')
    print(f'В полученной вершине значение целевой функции = {x_center[-1]}\n')
    print('Вычислим 𝜎 (сигма)')
    sigma = 0
    for i in range(len(mass)):
        if i not in mass_maximum:
            sigma += (mass[i][-1] - x_center[-1]) ** 2
    sigma = sigma / (n + 1)
    sigma = round(math.sqrt(sigma), 5)
    if sigma < e:
        print(f'Сигма = {sigma} < {e}')
        print('Так как условие окончания поиска выполняется, то процесс итераций завершен.')
    else:
        print(f'Сигма = {sigma} >= {e}')
        print('Так как условие окончания поиска не выполняется, то процесс итерации должен быть продолжен.')


def new_polyhedron(mass, mass_maximum, min_mean_max):
    for k in range(n):
        new = [0, 0]
        for l in range(n):
            new[l] = round(mass[min_mean_max[0][1]][l] + 0.5 *
                           (mass[mass_maximum[-2 + k]][l] - mass[min_mean_max[0][1]][l]), 5)
            print(f'{new[l]} = {mass[min_mean_max[-1][1]][l]} + 0.5 * ({mass[mass_maximum[-2 + k]][l]} - '
                  f'({mass[min_mean_max[-1][1]][l]}))')
        new.append(count_target_function(new[0], new[1]))
        print(f'Новые координаты = [{new[0]}; {new[1]}]')
        print(f'Целевая функция равна: {new[-1]}\n')
        mass.append(new)


def simplex_compressions(mass, mass_maximum, center_g, y):
    print('\nВыполним операцию сжатия симплекса:')
    new_coordinate_compressions = [0, 0]
    for i in range(len(new_coordinate_compressions)):
        print(f'X{len(mass) - 1}[{i}] = {center_g[i]} + {y} *'
              f' ({mass[-1][i]} - ({center_g[i]}))')

        new_coordinate_compressions[i] = round(center_g[i] + y * (mass[-1][i] - center_g[i]), 5)
    target_func = count_target_function(new_coordinate_compressions[0], new_coordinate_compressions[1])
    new_coordinate_compressions.append(target_func)

    print(f'\nПолучаем точку с координатами: [{new_coordinate_compressions[0]}; {new_coordinate_compressions[1]}]')
    print(f'В полученной вершине значение целевой функции = {new_coordinate_compressions[-1]}')
    return new_coordinate_compressions


def simplex_stretching(mass, mass_maximum, center_g, B):
    print('\nВыполним операцию растяжения симплекса:')
    new_coordinate_stretching = [0, 0]
    for i in range(n):
        print(f'x{len(mass)} = {center_g[i]} + {B} *'
              f' ({mass[-1][i]} - {center_g[i]})')
        new_coordinate_stretching[i] = round(center_g[i] + B * (mass[-1][i] - center_g[i]), 5)
    target_func = count_target_function(new_coordinate_stretching[0], new_coordinate_stretching[1])
    new_coordinate_stretching.append(target_func)
    print(f'Получаем точку с координатами: [{new_coordinate_stretching[0]}; {new_coordinate_stretching[1]}]')
    print(f'И функцией = {target_func}')
    return new_coordinate_stretching


def changing_the_function(mass, mass_maximum, new_coordinate, min_mean_max):  # уменьшается функция или увеличивается
    if new_coordinate[-1] < mass[min_mean_max[-1][1]][-1]:
        print(f'Наблюдается уменьшение целевой функции:')
        print(f'x{len(mass)} < x{min_mean_max[-1][1]}')
        print(f'{round(new_coordinate[-1], 5)} < {round(mass[mass_maximum[-1]][-1], 5)}')
        mass.append(new_coordinate)
        return True
    elif new_coordinate[-1] > mass[min_mean_max[-1][1]][-1]:
        print(f'Наблюдается увеличение целевой функции:')
        print(f'x{len(mass)} > x{min_mean_max[-1][1]}')
        print(f'{round(new_coordinate[-1], 5)} > {round(mass[mass_maximum[-1]][-1], 5)}\n\n')
        return False


def generate_new_point(mass, mass_maximum, minimum):
    k = -1
    while k != -5:
        new_coordinate = [0] * n
        for j in range(n):
            new_coordinate[j] = mass[minimum[1]][j] + 0.5 * (mass[k][j] - mass[minimum[1]][j])
        new_coordinate.append(count_target_function(new_coordinate[0], new_coordinate[1]))
        print(f'Новая точка с координатами x1 = {round(new_coordinate[0], 5)}, x2 = {round(new_coordinate[1], 5)}')
        print(f'В полученной вершине значение целевой функции = {round(new_coordinate[-1], 5)}')
        mass.append(new_coordinate)
        k -= 2


def find_minimum_value(mass, mass_maximum):
    minimum = [1000000, 0]
    for i in range(len(mass)):
        if mass[i][-1] < minimum[0] and i not in mass_maximum:
            minimum = [mass[i][-1], i]
    print(f'Берём минимальную функцию = {round(minimum[0], 5)}, номер вершины = {minimum[1]}\n')
    for i in range(len(mass)):
        if i != minimum[-1] and i not in mass_maximum:
            mass_maximum.append(i)
    return minimum


def condition_for_the_end_of_the_search(mass, e, mass_maximum):
    mass_center_gravity_simplex = []
    mass_coof = []
    for j in range(3):
        minimum = [100000, 0]
        for i in range(len(mass)):
            if mass[i][-1] < minimum[0] and i not in mass_coof and i not in mass_maximum:
                minimum = [mass[i][-1], i]
        mass_coof.append(minimum[1])
        mass_center_gravity_simplex.append(minimum)

    print(mass_center_gravity_simplex)

    x_center = [0, 0]
    for i in range(len(mass_center_gravity_simplex)):
        x_center[0] += mass[mass_center_gravity_simplex[i][1]][0]
        x_center[1] += mass[mass_center_gravity_simplex[i][1]][1]
    for i in range(len(x_center)):
        x_center[i] = round(x_center[i] / 3, 5)
    x_center.append(count_target_function(x_center[0], x_center[1]))
    print(f'Центер тяжести = [{x_center[0]}, {x_center[1]}]')
    print(f'В полученной вершине значение целевой функции = {x_center[-1]}\n')

    sigma = 0
    for i in range(len(mass_center_gravity_simplex)):
        sigma += (mass[mass_center_gravity_simplex[i][1]][-1] - x_center[-1]) ** 2
    sigma = sigma / (n + 1)
    sigma = round(math.sqrt(sigma), 5)
    if sigma < e:
        print(f'Сигма = {sigma} < {e}')
        print('Так как условие окончания поиска выполняется, то процесс итераций завершен.')
        return True
    else:
        print(f'Сигма = {sigma} >= {e}')
        print('Так как условие окончания поиска не выполняется, то процесс итерации должен быть продолжен.\n\n')
        return False


if __name__ == '__main__':
    min_mean_max = [1000000, 0, -1000000]
    mass_maximum = []
    mass = [[9, 9]]
    n = len(mass[0])  # размерость
    m = 0.25  # длина ребра симплекса
    B = 2.8  # параметр растяжения
    y = 0.4  # параметр сжатия
    e = 0.00001  # точность

    calculate_increments(mass, m, n)  # расчёт изначальныйх точек
    for i in range(len(mass)):  # расчёт изначальныйх функций для точек
        value_func = count_target_function(mass[i][0], mass[i][1])
        mass[i].append(value_func)

    table_output(mass)  # вывод таблицы

    iteration = 0
    while iteration is not True:
        # while iteration != 3:
        print('=' * 100)
        print('Итерация =', iteration)
        iteration += 1
        print('=' * 100)
        determination_of_min_mean_max(min_mean_max, mass, mass_maximum)  # находим минимум максимум и среднее значение

        maximum_value_function(mass, mass_maximum)  # отбераем максимальную точку

        center_g = center_of_gravity(mass, mass_maximum)  # находим центер

        new_coordinate = finding_coordinates_reflected_vertex(mass, mass_maximum,
                                                              center_g, min_mean_max)  # получем новые коодинаты точки

        if changing_the_function(mass, mass_maximum, new_coordinate,
                                 min_mean_max):  # наблюдается ли уменьшение целевой функции?
            if condition_fulfillment(mass, mass_maximum, min_mean_max, new_coordinate):
                new_coordinate_compressions = simplex_compressions(mass, mass_maximum, center_g, y)
                if new_coordinate_compressions[-1] < min_mean_max[-1][0]:
                    print('\n\nУчитывая, что условие сжатия выполнено,')
                    print(f'           x{len(mass)} < x{min_mean_max[-1][1]}')
                    print('то добавим значение в таблицу')
                    mass.append(new_coordinate_compressions)
                    table_output(mass)
                    if condition_for_the_end_of_the_search(mass, e, mass_maximum):
                        iteration = True
                else:
                    for i in range(len(mass) - 1):
                        if i not in mass_maximum:
                            mass_maximum.append(i)
                    print('\n\nУсловие растяжения не выполнено')
                    print(f'\nСформируем новый многогранник с уменьшенными вдвое сторонами и вершиной x{len(mass) - 1}')
                    new_polyhedron(mass, mass_maximum, min_mean_max)  # генерация нового многоугольника
                    if condition_for_the_end_of_the_search(mass, e, mass_maximum):  # условие окончание поиска
                        iteration = True
            else:
                new_coordinate_stretching = simplex_stretching(mass, mass_maximum, center_g, B)
                if new_coordinate_stretching[-1] < mass[-1][-1]:
                    print('\n\nУсловие растяжения выполнено')
                else:
                    for i in range(len(mass) - 1):
                        if i not in mass_maximum:
                            mass_maximum.append(i)
                    print('\n\nУсловие растяжения не выполнено')
                    print(f'\nСформируем новый многогранник с уменьшенными вдвое сторонами и вершиной x{len(mass) - 1}')
                    new_polyhedron(mass, mass_maximum, min_mean_max)  # генерация нового многоугольника
                    if condition_for_the_end_of_the_search(mass, e, mass_maximum):  # условие окончание поиска
                        iteration = True
        else:
            mass_maximum.append(min_mean_max[1][1])
            mass_maximum.append(min_mean_max[-1][1])
            new_polyhedron(mass, mass_maximum, min_mean_max)
            if condition_for_the_end_of_the_search(mass, e, mass_maximum):  # условие окончание поиска
                iteration = True

    table_output(mass)
