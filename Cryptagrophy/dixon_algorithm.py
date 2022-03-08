from math import gcd, sqrt #needed to compute sqrt(N) and gcd of pairs
import numpy as np # To use for numpy arrays
  
def dixons_algorithm(N):
    """The Dixon factorization algorithm"""
  
    P = [2, 3, 5, 7, 11, 13, 17, 19] # Primes less than or equal to B (20)
    start = int(sqrt(N)) # Finds root of N
    pairs = [] # Storing pairs or related squares
  
    for i in range(start, N): # Iterates through start until N
        for j in range(len(P)): # Look for related squares
            LS = i**2 % N
            RS = P[j]**2 % N
            if(LS == RS): # If numbers are related squares; appent to array
                pairs.append([i, P[j]])
  
    new = []
  
    for i in range(len(pairs)): # Computes GCD for the related squares
        factor = gcd(pairs[i][0] - pairs[i][1], N)
        if(factor != 1): # Factors that are not 1 gets appended to array
            new.append(factor)
    related_squares = np.array(new)
  
    return(np.unique(related_squares)) # Returns the unique factors of array

    
# Value of N to be used in Dixon's algorithm
print(dixons_algorithm(805957)) 
    
    
    
    
    