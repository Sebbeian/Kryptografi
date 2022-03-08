import random

def modulo(base, exponent, mod):
    """ Modulo function to perform binaryxponentiation """
    x = 1;
    y = base;
    while (exponent > 0):
        if (exponent % 2 == 1):
            x = (x * y) % mod;
        y = (y * y) % mod;
        exponent = exponent // 2;
    return x % mod;
 
def Jacobi(a, n):
    """ Computing Jacobi symbol """
    if (a == 0):
        return 0;# (0/n) = 0 
    ans = 1;
    if (a < 0):# (a/n) = (-a/n)*(-1/n)
        a = -a; # swap
        if (n % 4 == 3): # (-1/n) = -1 if n = 3 (mod 4)
            ans = -ans; # swap
    if (a == 1):
        return ans; # (1/n) = 1 
    while (a):
        if (a < 0):# (a/n) = (-a/n)*(-1/n)
            a = -a;
            if (n % 4 == 3):# (-1/n) = -1 if n = 3 (mod 4)
                ans = -ans;
        while (a % 2 == 0):
            a = a // 2;
            if (n % 8 == 3 or n % 8 == 5):
                ans = -ans;
        a, n = n, a;
        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans; 
        a = a % n;
        if (a > n // 2):
            a = a - n;
    if (n == 1):
        return ans;
    return 0;

 

def solovoy_Strassen_Prime_test(p, iterations):
    """ The Solovay-Strassen primality Test """
    if (p < 2):
        return False;
    if (p != 2 and p % 2 == 0):
        return False;
 
    for i in range(iterations):
        a = random.randrange(p - 1) + 1; # Generate a random number a
        jacobi = (p + Jacobi(a, p)) % p;
        mod = modulo(a, (p - 1) / 2, p);
 
        if (jacobi == 0 or mod != jacobi):
            return False;
    return True;
 
""" Enter value to test """
iterations = 20;
number = ((2**127) - 1); #2^127 - 1

if (solovoy_Strassen_Prime_test(number, iterations)):
    print(number, "is prime ");
else:
    print(number, "is composite");
 
