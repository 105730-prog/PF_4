def cub_root(n):
    # init the var
    x = n
    y = (2 * x + n / x**2) / 3
 
    # and iterate
    while abs(x - y) >= 0.00000001:
        x = y
        y = (2 * x + n / x**2) / 3
 
    return y
 
n = 711
print("Cubic root of", n, "is", round(cub_root(n), 6))