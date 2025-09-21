def average(num: list):
    count = 0
    sum = 0
    for i in num:
        if isinstance(i, (int, float)):
            sum += i
            count += 1
    return sum/count


def factorial(n):
    try:
        if n >= 0:
            if n <= 1:
                return 1
            else:
                return n * factorial(n-1)
    except ValueError:
        print('error value')


def quadratic_equation():
    pass
