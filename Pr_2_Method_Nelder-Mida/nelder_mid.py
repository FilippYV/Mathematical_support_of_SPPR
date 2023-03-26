import math


def calculate_increments(mass, m, n):
    print(mass, m, n)
    d1 = round(((math.sqrt(n + 1) - 1) / (n * math.sqrt(2))) * m, 3)
    print(f'd1 = ({(math.sqrt(n + 1) - 1)} / {(n * math.sqrt(2))}) * {m}')
    print('d1 =', d1, '\n')

    d2 = round(((math.sqrt(n + 1) + n - 1) / (n * math.sqrt(2))) * m, 3)
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
            print(f'{round(mass[i][j], 3)} | ', end='')
        print(f'{round(mass[i][-1], 3)}', end='')
        print()
    print()


def count_target_function(x, y):
    target_function = 10 * x ** 2 + 3 * x * y + y ** 2 + 10 * y  # 7
    # target_function = (2 * x ** 2) - 2 * x * y + (3 * y ** 2) + x - 3 * y  # 6
    # target_function = x**2 - x*y + 3*y**2-x
    # target_function = 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y
    return target_function


def maximum_value_function(mass, mass_maximum):
    maximum = [-99999999, 0]
    for i in range(len(mass)):
        if mass[i][-1] > maximum[0] and i not in mass_maximum:
            maximum = [mass[i][-1], i]
    print(f'Максимум функции = {round(maximum[0], 3)}, номер вершины = {maximum[1]}')
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
    print(f'Центер тяжести = [{round(x_center[0], 3)}, {round(x_center[1], 3)}]')
    print()
    return x_center


def finding_coordinates_reflected_vertex(mass, mass_maximum, center_g):
    new_coordinate = []
    for i in range(n):
        new_coordinate.append(2 * center_g[i] - mass[mass_maximum[-1]][i])
    print(f'Новые координаты = [{round(new_coordinate[0], 3)}; {round(new_coordinate[1], 3)}]')
    target_func = count_target_function(new_coordinate[0], new_coordinate[1])
    print('Целевая функция =', round(target_func, 3), '\n')
    new_coordinate.append(target_func)
    table_output(mass)
    return new_coordinate


def increased_or_decreased(mass, mass_maximum, new_coordinate, e, n): # уменьшается функция или увеличивается
    # print(mass)
    if new_coordinate[-1] < mass[mass_maximum[-1]][-1]:
        print(f'Наблюдается уменьшение целевой функции:')
        print(f'   x{len(mass) + 1} < x{mass_maximum[-1]}')
        print(f'{round(new_coordinate[-1], 3)} < {round(mass[mass_maximum[-1]][-1], 3)}')
        mass.append(new_coordinate)
        return condition_of_the_end_search(mass, mass_maximum, e, n)
    elif new_coordinate[-1] > mass[mass_maximum[-1]][-1]:
        print(f'Наблюдается увеличение целевой функции:')
        print(f'   x{len(mass) + 1} < x{mass_maximum[-1]}')
        print(f'{round(new_coordinate[-1], 3)} > {round(mass[mass_maximum[-1]][-1], 3)}')
        mass_maximum.append(len(mass) - 1)
        minimum = find_minimum_value(mass, mass_maximum)
        generate_new_point(mass, mass_maximum, minimum)
        return condition_of_the_end_search(mass, mass_maximum, e, n)


def generate_new_point(mass, mass_maximum, minimum):
    k = -1
    while k != -5:
        new_coordinate = [0] * n
        for j in range(n):
            new_coordinate[j] = mass[minimum[1]][j] + 0.5 * (mass[k][j] - mass[minimum[1]][j])
        new_coordinate.append(count_target_function(new_coordinate[0], new_coordinate[1]))
        print(f'Новая точка с координатами x1 = {round(new_coordinate[0], 3)}, x2 = {round(new_coordinate[1], 3)}')
        print(f'И целевой функцией = {round(new_coordinate[-1], 3)}')
        mass.append(new_coordinate)
        k -= 2


def find_minimum_value(mass, mass_maximum):
    minimum = [1000000, 0]
    for i in range(len(mass)):
        if mass[i][-1] < minimum[0] and i not in mass_maximum:
            minimum = [mass[i][-1], i]
    print(f'Берём минимальную функцию = {round(minimum[0], 3)}, номер вершины = {minimum[1]}\n')
    for i in range(len(mass)):
        if i != minimum[-1] and i not in mass_maximum:
            mass_maximum.append(i)
    return minimum


def condition_of_the_end_search(mass, mass_maximum, e, n): # подсчитывам критерии для остановки
    center_sim = []
    for j in range(n):
        coordinate = 0
        for i in range(len(mass)):
            if i not in mass_maximum:
                coordinate += mass[i][j]
        coordinate = round(coordinate / 3, 3)
        center_sim.append(coordinate)
    target = count_target_function(center_sim[0], center_sim[1])
    print(f'Центор тяжести симплекса: [{round(center_sim[0], 3)}, {round(center_sim[1], 3)}]')
    print(f'Функция в точке: {round(target, 3)}')
    print()
    count_f = 0
    count_true = 0
    for i in range(len(mass)):
        if i not in mass_maximum:
            print(f'Функция для {i} вершины = {round(mass[i][-1], 3)}')
            print(f'{round(mass[i][-1] - target, 3)} = {round(mass[i][-1], 3)} - ({round(target, 3)})')
            funck = round(mass[i][-1] - target, 3)
            count_f += 1
            if abs(funck) < e:
                print('|funck| < e')
                print(f'{abs(funck)} < {e}')
                count_true += 1
            else:
                print('|funck| > e')
                print(f'{abs(funck)} > {e}')
            print()
    print(f'{count_true} / {count_f} меньше\n')
    return count_f == count_true


if __name__ == '__main__':
    mass_maximum = []
    mass = [[0, 0]]
    n = len(mass[0])  # размерость
    m = 0.75  # длина ребра симплекса
    B = 1.85 # параметр растяжения
    y = 0.1 # параметр сжатия
    e = 0.1 # точность

    calculate_increments(mass, m, n)  # расчёт изначальныйх точек
    exit(1)
    for i in range(len(mass)):  # расчёт изначальныйх функций для точек
        value_func = count_target_function(mass[i][0], mass[i][1])
        mass[i].append(value_func)

    table_output(mass)  # вывод таблицы

    iteration = 0
    while iteration is not True:
        print('=' * 100)
        print('Итерация =', iteration)
        iteration += 1
        print('=' * 100)
        maximum_value_function(mass, mass_maximum)  # отбераем максимальную точку
        center_g = center_of_gravity(mass, mass_maximum)  # находим центер
        new_coordinate = finding_coordinates_reflected_vertex(mass, mass_maximum,
                                                              center_g)  # получем новые коодинаты точки
        if increased_or_decreased(mass, mass_maximum, new_coordinate, e, n):
            print('-' * 100)
            print('Так как все условия окончания поиска выполняются, то процесс итерации завершен.')
            print(
                f'В качестве приближенного решения x выбирается \nx{len(mass) - 1} = [{round(mass[-1][0], 3)};'
                f' {round(mass[-1][1], 3)}]\n'
                f'которой соответствует наименьшее значение целевой функции x{len(mass) - 1} = {round(mass[-1][-1], 3)}')
            print('-' * 100)
            iteration = True
        else:
            print('-' * 100)
            print('Так как все условия окончания поиска не выполняются, то процесс итераций должен быть продолжен!')
            print('-' * 100)
            print()
    table_output(mass)
