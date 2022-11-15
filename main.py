from numbers import Number
from typing import Callable


def censor(s: str, blacklist: list[str]):
    for elem in blacklist:
        s = s.replace(elem, '*' * len(elem))
    return s


def shorten(s: str, size: int):
    s = s.lower()
    s = s.replace(' ', '-')
    n = len(s)
    k = n - size + 2
    p = (n - k) // 2
    if size % 2 != 0:
        return s[0:p] + '...' + s[(n - p):n]
    else:
        return s[0:p] + '..' + s[(n - p):n]


def windowed_average(array: list[Number], k: int):
    ans = []
    # переберем позицию i -- начало окна
    for i in range(len(array) - k + 1):
        window_sum = 0.0
        # переберем все элементы в окне [i, i + k]
        for j in range(k):
            window_sum += array[i + j]
        ans.append(window_sum / k)
    return ans


def rprint(array: list, max_depth: int):
    if max_depth <= 0:
        return '[...]'
    s = '['
    for i in range(len(array)):
        elem = array[i]
        if type(elem) is list:
            s += rprint(elem, max_depth - 1)
        else:
            s += str(elem)
        if i != len(array) - 1:
            s += ', '
    s += ']'
    return s


def median(*args: int, low: bool = True):
    lst = list(args)
    lst.sort()
    # print(lst)
    n = len(lst)
    if n % 2 != 0:
        return lst[(n - 1) // 2]
    if low:
        return lst[(n // 2) - 1]
    return lst[(n // 2)]


def logging(f0: Callable):
    def g0(*args, **kwargs):
        print(args, kwargs)
        return f0(*args, **kwargs)

    return g0


def test(number, x, y):
    # print(number, ':', x)
    print(number, ':', x == y)


if __name__ == '__main__':
    print('hello world!')

    test(
        1,
        censor('Hello, world!', ['world']),
        'Hello, *****!'
    )

    test(
        2,
        censor('I am inevitable', ['I', 'inevi']),
        '* am *****table'
    )

    test(
        3,
        shorten('World', 4),
        'w..d'
    )

    test(
        4,
        shorten('Task number 1 Data', 15),
        'task-n...1-data'
    )

    test(
        5,
        windowed_average([1, 3, 5, 7, 9], 2),
        [2.0, 4.0, 6.0, 8.0]
    )

    test(
        6,
        windowed_average([1, 5, 7, 10, 18], 4),
        [5.75, 10.0]
    )

    test(
        7,
        rprint([1, [2], [[3]], [[[4]]]], 2),
        '[1, [2], [[...]], [[...]]]'
    )

    test(
        8,
        rprint([1, [2, 3], [[4, [5], [6, [7], [[[8]]]]]], [9]], 3),
        '[1, [2, 3], [[4, [...], [...]]], [9]]'
    )

    test(
        9,
        rprint([1, 2, 3], 0),
        '[...]'
    )

    test(
        10,
        median(4, 3, 5, 1, 2),
        3
    )

    test(
        11,
        median(6, 2, 1, 4, 5, 3),
        3
    )

    test(
        12,
        median(6, 2, 1, 4, 5, 3, low=False),
        4
    )


    def f(x1, y1, z1, opt=False):
        if opt:
            return max(x1, y1, z1)
        return min(x1, y1, z1)


    g = logging(f)
    x2 = g(1, 2, 3, opt=True)
    y2 = g(6, 5, 4)

    print('(1, 2, 3), {\'opt\': True}')
    print('(6, 5, 4), {}')

    test(13, x2, 3)
    test(14, y2, 4)
