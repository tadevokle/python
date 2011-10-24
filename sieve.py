# The following implmenetation of the sieve of Erathosthenes is implemented for artistic purposes
# only. [Although it performs relatively well for input <= 10 ** 6
#
#
#Author: Vedat Levi Alev


def sieve_of_erathosthenes(limit):
    """Returns a list primes in the intervall [2,limit)"""
    sieve = range(2,limit)
    primes = []
    fin = int(limit**(0.5))
    while sieve[0] < fin:
        primes.append(sieve[0])
        sieve = filter(lambda x : x % sieve[0], sieve)
    return primes+sieve

print sieve_of_erathosthenes(30)
