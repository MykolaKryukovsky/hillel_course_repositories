
def common_elements():
    multiples_three= {x for x in range(100) if x % 3 == 0}
    multiples_five = {x for x in range(100) if x % 5 == 0}
    multiples_three_five = multiples_three.intersection(multiples_five)
    return f" common_elements() == {multiples_three_five}"

common_elements()