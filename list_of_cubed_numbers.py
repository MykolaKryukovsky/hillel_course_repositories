from inspect import isgenerator

#F(n) = O(n)
def generate_cube_numbers(end) -> Generator[int]:
    """
    numbers in a cube from first i > end
    :param end: int
    :return: Generator[int]
    """
    cube_numbers = []
    for i in range(2, end + 1):
        cube =  i ** 3
        if cube > end:
            break
        else:
            cube_numbers.append(cube)
    for c in range(len(cube_numbers)):
        yield cube_numbers[c]


gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print('OK')