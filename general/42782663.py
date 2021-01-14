# Посылка 42782663

def hasCycle(node):
    ''' Функция проверки наличия зацикливания ссылок в односвязном списке

    На вход принимает элемент класса Node.
    Алгоритм работает по принципу двух указателей, которые бегают по элментам.
    Первый указатель за каждую итерацию цикла функции смещается на 2 элемента,
    второй на 1.
    Цикл обнаруживается, если более быстрый указатель (заяц) догоняет более
    медленный (черепаха).
    Если указатель заяц доходит до конца списка, то цикла нет.
    '''
    if node.next is None:
        return False
    hare = node.next  # заяц
    turtle = node  # черепаха

    while (hare is not None
           and hare.next is not None):
        if hare is turtle:
            return True
        turtle = turtle.next
        hare = hare.next
        if hare.next is not None:
            hare = hare.next
    return False
