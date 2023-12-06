s = input('Введите числа через пробел: ')
element = float(input('Введите требуемое число: '))
array = list(map(float, s.split()))
print('Массив получен',array)
def sort():
    for i in range(len(array)):  # проходим по всему массиву
        idx_min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            array[i], array[idx_min] = array[idx_min], array[i]
    print('Массив отсортирован',array)
sort()
def search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] >= element and array[middle - 1] < element:  # если элемент в середине,
        return middle - 1  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return search(array, element, left, middle - 1)
    else:  # иначе в правой
        return search(array, element, middle + 1, right)

print('Номер позиции искомого числа:')
print(search(array,element,0,len(array)))