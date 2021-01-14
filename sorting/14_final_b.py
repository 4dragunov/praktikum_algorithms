# Посылка 44653501
from typing import List


def radix_sort(arr: List[int]) -> List[int]:
    '''
    Функция устойчивой поразрядной сортировки.

    На каждой итерации происходит устойчивая сортировка по каждому разряду
    (от едениц и до самого большого разряда)
    '''
    max_lenght = len(str(max(arr)))  # максимальная длинна элемента массива
    rang = 10  # количество возможных цифр у каждого разряда
    for level in range(max_lenght):
        temp_arr = [[] for i in range(rang)]
        for number in arr:
            x = number // 10 ** level % 10
            temp_arr[x].append(number)
        arr = []
        for item in range(rang):
            arr = arr + temp_arr[item]
    return arr


def main():
    '''
    В качестве входнный данных:
    1 строка - длина массива
    2 строка - массив (строка) неотрицательных простых чисел, каждое из
    который <= 100000
    '''
    try:
        num_cnt = int(input())
        arr = list(map(int, input().rstrip().split()))
    except ValueError:
        print('Ошибка ввода')
    assert num_cnt == len(arr), 'Ошибка ввода массива'

    print(*radix_sort(arr))


if __name__ == '__main__':
    main()
