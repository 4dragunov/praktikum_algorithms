# Посылка 42781881
import operator


class Stack:
    '''Стэк для записи и извлечения операндов и результатов калькуляции

    Поддерживает метод push - добавление элемента (int) в стэк и pop -
    извлечение
    элемента (с последующим удалением)
    '''

    def __init__(self):
        self.__items = []

    def push(self, item) -> object:
        '''Добавление числа в стек'''
        self.__items.append(int(item))

    def pop(self):
        '''Извлечение и удалением элемента из стека'''
        try:
            return self.__items.pop()
        except IndexError:
            raise IndexError('pop from empty stack')


# словарь для хранения операций и методов
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


def calc(act: str, stack: Stack):
    '''Функция калькуляции.

    На вход принимает одно из значений OPERATORS (+, -, /, *) и объект
    класса стэк (инициализированный при запуске __main__)
    Извлекает из стека два последних записанных элемента и произодит
    математическую операцию переданную при вызове через operator.
    Результат добавляет в стэк.
    '''
    last = stack.pop()
    first = stack.pop()
    result = OPERATORS[act](first, last)
    stack.push(result)


def remove_prefix(text):
    '''Функция удаления знака '-' перед числом '''

    if text.startswith('-'):
        return text[len('-'):]
    return text


if __name__ == '__main__':
    stack = Stack()
    for char in list(input().split()):
        if char in OPERATORS.keys():
            calc(char, stack)
        elif remove_prefix(char).isnumeric():
            stack.push(char)
        else:
            print('error')

    print(stack.pop())
