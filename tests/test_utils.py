from slink.utils import is_prime


def test_primes():
    known_primes = (3, 19, 21937)
    for number in known_primes:
        assert is_prime(number), f'{number} is supposed to be prime.'
