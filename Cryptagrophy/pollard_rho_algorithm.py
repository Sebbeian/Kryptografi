from math import gcd
import random

def pollard_rho_algorithm(N):
    """ Pollard's rho algorithm (p-method)"""
    if N % 2 == 0: # if N modulo 2 is 0
            return 2
        
    x = random.randint(1, N-1) # returns a number between 1 and N-1 (both included)
    y = x
    z = random.randint(1, N-1) # returns a number between 1 and N-1 (both included)
    p = 1
    while p == 1:             
            x = ((x*x) % N + z) % N # sets x to (x times x mod N + z) mod N
            y = ((y*y) % N + z) % N 
            y = ((y*y) % N + z) % N
            p = gcd(abs(x - y), N) # GCD of absolute value of (x-y) and N
    return p


# Value of N to be used in Pollard's rho algorithm
print(pollard_rho_algorithm(1096478806896662720778610291))




