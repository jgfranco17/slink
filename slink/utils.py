"""Helper module for miscellaneous calculations."""

import math


def is_prime(number: int) -> bool:
    """Checks to see if a number is a prime in O(sqrt(n))."""

    # precondition
    if not (isinstance(number, int) and (number >= 0)):
        raise ValueError("Value of 'number' must been an int and positive")

    if 1 < number < 4:
        # 2 and 3 are primes
        return True
    elif number < 2 or not number % 2:
        # Negatives, 0, 1 and all even numbers are not primes
        return False

    odd_numbers = range(3, int(math.sqrt(number) + 1), 2)
    return not any(not number % i for i in odd_numbers)


def next_prime(value, factor=1, **kwargs):
    value = factor * value
    first_value_val = value

    while not is_prime(value):
        value += 1 if not ("desc" in kwargs and kwargs["desc"] is True) else -1

    if value == first_value_val:
        return next_prime(value + 1, **kwargs)
    return value
