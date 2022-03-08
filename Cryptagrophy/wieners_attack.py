from typing import Iterable


def wiener_attack(e, N): # Break RSA with computing of N and e
    """Wieners attack"""
    rtcf = rational_to_continued_fractions(e, N)
    for k, dg in convergents_from_continued_fractions(rtcf):
        edg = e*dg
        phi = edg//k
        i = N - phi + 1
        
        if i % 2 == 0 and perfect_square((i//2)**2 - N):
            g = edg - phi*k
            return dg//g
    return None


def integer_square_root(N): # Finds square root of N
    if N == 0:
        return 0
    
    i = 2**((N.bit_length() + 1)//2)
    
    while True:
        j = (i + N // i)//2
        if j >= i:
            return i
        i = j


def perfect_square(N): # Checks if it is perfect square 
    mod256 = (1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
                 1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
                 0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
                 0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0)
    
    if mod256[N & 0xff] == 0: # N & Hexadeicmal for base 16 (11111111 in binary) mod256
        return False

    mt = ((9,(1,1,0,0,1,0,0,1,0)),(5,(1,1,0,0,1)),(7,(1,1,1,0,1,0,0)),(13,(1,1,0,1,1,0,0,0,0,1,1,0,1)),(17,(1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1)))
    a = N % (9*5*7*13*17) # N modulo m
    
    if any(t[a % m] == 0 for m, t in mt):
        return False
    return integer_square_root(N)**2 == N 


def rational_to_continued_fractions(i,j): #Euclid's algorithm & continued fractions
    while j:
        a = i//j
        yield a
        i,j = j,i - a*j
        

def convergents_from_continued_fractions(continued_fractions: Iterable[int]): # Continued fraction algorithm
    N_, d_ = 1, 0
    for i, (N, d) in enumerate(continued_fractions_to_rational(continued_fractions)):
        if i % 2 == 0:
            yield N + N_, d + d_
        else:
            yield N, d
        N_, d_ = N, d
        
            
def continued_fractions_to_rational(continued_fractions: Iterable[int]): # Continued fraction algorithm
    n0, d0 = 0, 1
    n1, d1 = 1, 0
    for q in continued_fractions:
        N = q * n1 + n0
        d = q * d1 + d0
        yield N, d
        n0, d0 = n1, d1
        n1, d1 = N, d


# Values for e and N to run in Wieners attack
print(wiener_attack(1019780502436124204526035803328433120546131480982513669063240298393724197157659719919974259213600826800914988178815738273,
                    1425225108873296200467113803219632795530932221093957012175185409440553760738268403886123386867226620153943341619157040813))


