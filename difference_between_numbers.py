

def  difference(*args) -> int | float:
    """
    This function returns the difference between two numbers
    :param args: int | float
    :return: int | float
    """
    if not args:
        return 0
    max_number = max(args)
    min_number = min(args)
    difference_arg = max_number - min_number
    if difference_arg % 2 != 0:
        return round(difference_arg , 1)
    else:
        return int(difference_arg)



print(difference(10.2, -2.2, 0, 1.1, 0.5))