import numpy as np

e = 13
n = 527

for p in range(1, 1 + int(np.sqrt(n))):
    if n % p == 0:
        q = n / p
        for d in range(n):
            if e*d % ((e-1)*(q-1)) == 1:
                print(p, q)
                print(d, e)
                

