## The following is implemented for artistic purposes only. Although it performs fairly fast for
## inputs <= 10**5 (under 1 second), starting from iput>= 10**6 things start to get scary (more than
## 10 seconds)
##
##
## Author : Vedat Levi Alev

def sieve_of_eratosthenes(limit):
    """Returns all the primes in the intervall [2:limit)"""
    assert type(limit) == type(0) and limit > 2, "input must be an integer greater than 2"
    sieve = range(2,limit)# this might cause some problems in python 3
    primes = []
    fin = int(limit**(0.5)) # a number cannot have a prime divisor greater than its square root
    while sieve[0] <= fin:
        p = sieve[0]
        primes.append(p)
        sieve = filter(lambda y: y % p, sieve)
    return primes + sieve #the remaining elements in the sieve cannot be composite numbers, see above

