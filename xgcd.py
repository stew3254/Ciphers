#!/usr/bin/python3

import sys

def xgcd(a,b, table=False):
        x0, y0, x1, y1 = 1, 0, 0, 1
        while b != 0:
            q = a // b
            r = a % b

            if table:
                # print(f"a:{a}, b:{b}, q:{q}, x0:{x0}, y0:{y0}, x1:{x1}, y1:{y1}")
                print(f"|{a}|{b}|{q}|{r}|{x0}|{y0}|{x1}|{y1}|")

            a, b = b, r
            x0, x1 = x1, x0 - q*x1
            y0, y1 = y1, y0 - q*y1
        return x0, y0


if __name__ == "__main__":
    a = 0
    b = 0

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} n1 n2")
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

    x, y = xgcd(a,b,True)

    print(f"a:{a}, b:{b}, x:{x}, y:{y}")
    print("ax + by = 1")
    print(f"({a})({x}) + ({b})({y}) = 1")

