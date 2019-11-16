#!/usr/bin/python3

import secrets
import math
from miller_rabin import miller_rabin
from xgcd import xgcd

class RSA:
    def __init__(self, *, p=None, q=None, n=None, e=None, k=512, l=10):
        # Make sure k is big enough to be a prime
        if k < 3:
            raise Exception("k must be at least 3")
        self.k = k

        if l < 1:
            raise Exception("l must be at least 1")
        self.l = l

        if n is not None:
            # Check if p and q are invalid for n
            if p is not None and q is not None:
                if p*q != n:
                    raise Exception("n must equal p*q")
                elif not miller_rabin(p, l) or not miller_rabin(q, l):
                    raise Exception("Please provide valid primes")
                self._p = p
                self._q = q
            # Check p is good for n
            elif p is not None:
                self.__validate_prime(p)
                self._p = p
                self._q = None
            # Check q is good for n
            elif q is not None:
                self.__validate_prime(q)
                self._p = None
                self._q = q
            else:
                self._p = None
                self._q = None
            self.n = n

        # Checks to see if e is valid
        # TODO supplying e by itself is a bit broken now
        if e is not None:
            if p is not None and q is not None:
                self._phi = (p-1)*(q-1)
                self.n = p*q
                self._d = self.__validate_e(e, self._phi)
                if self._d is None:
                    raise Exception("Please supply a valid e")
        self.e = e

        if p is not None and q is not None and n is None:
            if not miller_rabin(p, l) or not miller_rabin(q, l):
                raise Exception("Please provide valid primes")
            self._p = p
            self._q = q
            self._phi = (self._p - 1)*(self._q - 1)
            self.n = self._p * self._q
            if self.e is None:
                self.e, self._d = self.__gen_e_d(self._phi);
        elif n is None:
            if p is not None:
                if not miller_rabin(p, l):
                    raise Exception("Please provide a valid prime")
                self._p = p
                #Get number of bits
                self.k = int(math.log2(self._p))
                if self.e is None:
                    self._q, self._phi, self._d, self.e = self.__gen_valid_priv_keys(self._q)
                else:
                    self._q, self._phi, self._d = self.__gen_valid_priv_keys(self._q, self.e)
            elif q is not None:
                if not miller_rabin(q, l):
                    raise Exception("Please provide a valid prime")
                #Generate the rest of the keys
                if e is None:
                    self._p, self._phi, self._d, self.e = self.__gen_valid_priv_keys(self._q)
                else:
                    self._p, self._phi, self._d = self.__gen_valid_priv_keys(self._q, self.e)
            else:
                self.k = k
                #Generate p
                self._p = secrets.randbits(self.k)
                while not miller_rabin(self._p, l):
                    self._p = secrets.randbits(self.k)
                #Generate the rest of the keys
                if e is None:
                    self._q, self._phi, self._d, self.e = self.__gen_valid_priv_keys(self._p)
                else:
                    self._q, self._phi, self._d = self.__gen_valid_priv_keys(self._p, self.e)
            self.n = self._p * self._q

    # Generates a valid q based on given p and e
    # Returns q, phi, d and if was not given to the function, a valid e
    def __gen_valid_priv_keys(self, p, e=None):
        if e is not None:
            good = False
            while not good:
                q = secrets.randbits(self.k)
                while not miller_rabin(q, self.l):
                    q = secrets.randbits(self.k)
                phi = (p-1)*(q-1)
                n = p*q
                d = self.__validate_e(e, phi)
                if d is not None:
                    good = True
            return q, phi, d
        else:
            q = secrets.randbits(self.k)
            while not miller_rabin(q, self.l):
                q = secrets.randbits(self.k)
            phi = (p-1)*(q-1)
            n = p*q
            e, d = self.__gen_e_d(phi)
            return q, phi, d, e

    def __gen_e_d(self, phi):
        d = None
        e, d = 0, None
        while d is None:
            e = secrets.randbits(self.k) % phi
            d = self.__validate_e(e, phi)
        return e, d % phi

    def __validate_prime(self, p, n):
        if not miller_rabin(p, l):
            raise Exception("Please provide a valid prime")
        q = n/p
        if not miller_rabin(q, l):
            raise Exception("Prime is invalid for this n")

    def __validate_e(self, e, phi):
        x, y = xgcd(e, phi)
        if e*x + phi*y == 1:
            return x % phi
        return None

    def __isqrt(self, n):
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x

    def __factor(self, n):
        l = [(i, n//i) for i in range(3,int(self.__isqrt(n)+1),2) if n%i == 0]
        if len(l) == 1:
            return l[0]
        else:
            return None

    def priv_keys(self):
        return self._p, self._q, self._phi, self._d

    def pub_keys(self):
        return self.n, self.e

    # Only useful on small a small n
    def crack(self, n=None, phi=None):
        if n is None:
            n = self.n
        if phi is None:
            if self._p is None and self._q is None:
                self._p, self._q = self.__factor(n)
                return self._p, self._q
            return self.__factor(n)
        else:
            p_plus_q = n + 1 - phi
            p_minus_q = self.__isqrt(pow(p_plus_q, 2) - 4*n)
            p = (p_minus_q + p_plus_q)//2
            q = n//p
            return p, q

    def encrypt(self, m, n=None, e=None):
        if n is None:
            n = self.n
        if e is None:
            e = self.e

        if isinstance(m, str):
            return [pow(ord(c),e,n) for c in m]
        else:
            return [pow(int(c),e,n) for c in m]

    def decrypt(self, c):
        if self._p is None:
            raise Exception("Cannot decrypt without private keys")
        binary = [bin(pow(i, self._d, self.n))[2:] for i in c]
        binary = "".join(["0"*(8 - (len(i)%8)) + i for i in binary])
        return "".join([chr(int(binary[8*i:8*(i+1)], 2)) for i in range(len(binary)//8 - 1)])


if __name__ == "__main__":
    n, e = None, None
    c = None

    # Grab the hint keys
    with open("a2-hint.pubkeys", "r") as f:
        n = int(f.readline().strip())
        e = int(f.readline().strip())

    # Grabs encrypted phi
    with open("a2-hint.cipher", "r") as f:
        c = [int(i.strip()) for i in f.readlines()]
    # Creates new rsa
    r = RSA(n=n, e=e)
    # Encrypts each ASCII digit
    nums = r.encrypt("".join([chr(i) for i in range(ord("0"), ord("0")+10)]))
    # Finds phi through analysis of the numbers
    phi = int("".join([str(nums.index(i)) for i in c if i in nums]))

    # Grab the new n and e
    with open("a2.pubkeys", "r") as f:
        n = int(f.readline().strip())
        e = int(f.readline().strip())

    # Crack phi to get p and q
    p, q = r.crack(n, phi)

    # Create a new rsa object using the new keys
    r = RSA(p=p, q=q, e=e, n=n)

    # Grab the encrypted homework
    with open("a2.cipher", "r") as f:
        c = [int(i.strip()) for i in f.readlines()]

    # Decrypt the assignment
    with open("hw2.txt", "w") as f:
        f.write(str(r.decrypt(c)) + "\n")
