
def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
        start: the first element of the sequence
        end: the number of elements in the sequence
        func: a function that generates values for the sequence
    """
    for _ in range(end):
        yield begin
        begin = func(begin)

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')