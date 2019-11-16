import random

def miller_rabin(n, k):
    """Used to probably generate prime numbers very quickly"""
    if n == 2:
        return True
    if n < 2 or (n != 2 and n%2 == 0) or (n != 5 and n%5 == 0):
        return False

    r, d = 0, n - 1
    # Factor out 2**r * d + 1
    while d%2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        # Produce a witness
        a = random.randrange(1, n-1)
        x = pow(a, d, n)
        # n is probably prime
        if x == 1 or x == n-1:
            continue
        # Continue to check
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        # If not broken out of the loop n is definitely not prime
        else:
            return False
    # n has a 1/(2**k) chance of not being prime
    return True
