# Посылка 44652798
from typing import List


def max_number(arr: List[str], num_cnt: int) -> List[str]:
    '''
    Функция сортировки массива чисел для получения максимального значения
    последовательности

    За идею взят алгоритм сортировки "пузырьком".
    '''
    for i in range(num_cnt):
        for j in range(i, num_cnt):
            if int(arr[j] + arr[i]) > int(arr[i] + arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def main():
    '''
    Входные данные:
    1 строка - количество чисел < 100
    2 строка - массив (список) неотрицательных чисел, каждое из которых <= 1000
    '''
    try:
        num_cnt = int(input())
        arr = list(map(str, input().rstrip().split()))
    except ValueError:
        print('Ошибка ввода')
    assert num_cnt == len(arr), 'Ошибка ввода массива'

    print(*max_number(arr, num_cnt), sep='')


if __name__ == '__main__':
    main()
