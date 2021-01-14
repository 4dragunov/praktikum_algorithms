# id посылки 43519991
from typing import List


def count_items(capacity: List[int], amount_capacity: int) -> int:
    '''Функция подсчета максимального количества элементов, при выполнении
    условия - каждый элемент (фото) в 2х дата центрах.

    На вход принимает список вместимости датацентров и их количество.
    Принцип работы:
    -На каждой итерации (пока количество центров не меньше 2) кладем фото в
    датацентр с минимальным количеством слотов и с максимальным,
    сортируем данные, убираем из списка датацентры с 0.

    :param capacity: список вместимостей датацентров <= 10000
    :param amount_capacity: количество датацентров
    :return: Максимальное количество фотографий, для которых можно хранить
    копии в датацентрах
    '''
    result_count = 0

    while amount_capacity >= 2:
        capacity.sort(reverse=True)
        if capacity[-1] == 0:
            capacity.pop()
            amount_capacity -= 1
            continue
        capacity[0] -= 1
        capacity[-1] -= 1
        result_count += 1

    return result_count


def main():
    amount_capacity = int(input())
    capacity = list(map(int, input().split()))
    print(count_items(capacity, amount_capacity))


if __name__ == '__main__':
    main()
