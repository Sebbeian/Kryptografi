def Jacobi(a, n):
    """ Computing Jacobi symbol """
    if (a == 0):
        return 0;# (0/n) = 0 
    ans = 1;
    if (a < 0):# (a/n) = (-a/n)*(-1/n)
        a = -a;
        if (n % 4 == 3): # (-1/n) = -1 if n = 3 (mod 4)
            ans = -ans;
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
                ans = -ans;# swap
        a, n = n, a;
        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans;
        a = a % n;
        if (a > n // 2):
            a = a - n;
    if (n == 1):
        return ans;
    return 0;

print(Jacobi(-776439811,963110787895461237))





