mistake = 'Нужен перезапуск!!!!'
numbers = input('Введите числа через пробел: ')
user_number = int(input('Введите  число: '))


def is_int(line):
    line = line.replace(' ', '')
    try:
        int(line)
        return True
    except ValueError:
        return False


if " " not in numbers:
    print("\nОшибка введено без пробелов (Введите числа, через пробел.)")
    sequence_numbers = input('Введите  числа через пробел: ')
if not is_int(numbers):
    print('\nОшибка некорректный ввод (Введите числа, через пробел.)\n')
    print(mistake)
else:
    numbers = numbers.split()

list_numbers = [int(item) for item in numbers]


def merge_sort(d):
    if len(d) < 2:
        return d[:]
    else:
        middle = len(d) // 2
        left = merge_sort(d[:middle])
        right = merge_sort(d[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list_numbers = merge_sort(list_numbers)


def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Введено неверное число!'


print(f'Список по возрастанию : {list_numbers}')

if not binary_search(list_numbers, user_number, 0, len(list_numbers)):
    sosednee_chislo = min(list_numbers, key=lambda x: (abs(x - user_number), x))
    ind = list_numbers.index(sosednee_chislo)
    max_ind = ind + 1
    min_ind = ind - 1
    if sosednee_chislo < user_number:
        print(f'''В списке отсутствует введенное число 
Меньше введенного числа: {sosednee_chislo},  индекс: {ind}
Больше введенного числа: {list_numbers[max_ind]}  индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке отсутствует введенное число
Больше введенного числа: {sosednee_chislo},  индекс: {list_numbers.index(sosednee_chislo)}
В списке нет меньшего числа''')
    elif sosednee_chislo > user_number:
        print(f'''В списке отсутствует введенное число
Больше введенного числа: {sosednee_chislo},  индекс: {list_numbers.index(sosednee_chislo)}
Меньше введенного числа: {list_numbers[min_ind]}, индекс: {min_ind}''')
    elif list_numbers.index(sosednee_chislo) == 0:
        print(f'Индекс введенного числа: {list_numbers.index(sosednee_chislo)}')
else:
    print(f'Индекс введенного числа: {binary_search(list_numbers, user_number, 0, len(list_numbers))}')
